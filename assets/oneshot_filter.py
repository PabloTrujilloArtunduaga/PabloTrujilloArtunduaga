"""
World Machine color filter (OneShot) - Python port.

Algorithm and data (dataColors.txt) from MaxBuster380/OneShot-Color-Filter (MIT License):
https://github.com/MaxBuster380/OneShot-Color-Filter
The RGB cube is split into tetrahedra using the sample colors, and every pixel
is mapped by barycentric interpolation between the output colors.

Usage:
    pip install pillow numpy
    python oneshot_filter.py input.gif output.gif [--tv 2]
"""
import sys, os, argparse
import numpy as np
from PIL import Image, ImageSequence

HERE = os.path.dirname(os.path.abspath(__file__))

def det4(m):
    return int(round(np.linalg.det(np.array(m, dtype=float))))

def vol(v):  # same as Kotlin: |det| without the 1/6 factor
    m = [[v[i][0] for i in range(4)], [v[i][1] for i in range(4)],
         [v[i][2] for i in range(4)], [1, 1, 1, 1]]
    return abs(det4(m))

def cut(p, t):
    return [(p, t[1], t[2], t[3]), (p, t[0], t[2], t[3]),
            (p, t[0], t[1], t[3]), (p, t[0], t[1], t[2])]

def contains(t, p):
    return vol(t) == sum(vol(c) for c in cut(p, t))

def build_cube(path):
    rows, seen = [], set()
    for line in open(path):
        a = line.split()
        if len(a) == 6:
            i, o = tuple(map(int, a[:3])), tuple(map(int, a[3:]))
            if i not in seen:
                seen.add(i); rows.append((i, o))
    out = dict(rows)
    c = lambda *x: tuple(x)
    Z, X, Y, Zz = c(0,0,0), c(255,0,0), c(0,255,0), c(0,0,255)
    XY, XZ, YZ, XYZ = c(255,255,0), c(255,0,255), c(0,255,255), c(255,255,255)
    tets = [(Z,XYZ,XY,X),(Z,XYZ,XY,Y),(Z,XYZ,XZ,X),(Z,XYZ,XZ,Zz),(Z,XYZ,YZ,Y),(Z,XYZ,YZ,Zz)]
    corners = {Z,X,Y,Zz,XY,XZ,YZ,XYZ}
    for p, _ in rows:
        if p in corners: continue
        hit = [t for t in tets if contains(t, p)]
        for t in hit:
            tets.remove(t)
            tets += [s for s in cut(p, t) if vol(s) != 0]
    return tets, out

class Filter:
    def __init__(self, data=os.path.join(HERE, "dataColors.txt")):
        self.tets, self.out = build_cube(data)
        self.cache = {}

    def color(self, rgb):
        if rgb in self.cache: return self.cache[rgb]
        for t in self.tets:
            if contains(t, rgb):
                tv = vol(t)
                bary = [vol(c) / tv for c in cut(rgb, t)]
                res = tuple(int(round(sum(self.out[t[k]][ch] * bary[k] for k in range(4))))
                            for ch in range(3))
                self.cache[rgb] = res
                return res
        raise ValueError(f"no section for {rgb}")

    def apply(self, img, tv=2):
        img = img.convert("RGBA")
        a = np.array(img)
        rgb = a[..., :3]
        flat = rgb.reshape(-1, 3)
        uniq, inv = np.unique(flat, axis=0, return_inverse=True)
        mapped = np.array([self.color(tuple(int(v) for v in u)) for u in uniq], dtype=np.uint8)
        a[..., :3] = mapped[inv.reshape(-1)].reshape(rgb.shape)
        if tv > 0:  # TV effect: darken brightness (HSB) by 5/255 on alternating bands
            h = a.shape[0]
            # Same pattern as the Kotlin code: `tv` rows darkened, `tv` rows untouched
            rows = [y for y in range(h) if (y % (2 * tv)) < tv]
            f = a[..., :3].astype(float)
            sel = np.zeros(h, bool); sel[rows] = True
            mx = f[sel].max(axis=-1, keepdims=True)
            d = np.minimum(5.0, mx)
            scale = np.where(mx > 0, (mx - d) / np.maximum(mx, 1e-9), 1)
            f[sel] = f[sel] * scale
            a[..., :3] = np.clip(np.round(f), 0, 255).astype(np.uint8)
        return Image.fromarray(a, "RGBA")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input"); ap.add_argument("output")
    ap.add_argument("--tv", type=int, default=2, help="TV effect band thickness (0 = off)")
    s = ap.parse_args()
    flt = Filter()
    im = Image.open(s.input)
    if getattr(im, "is_animated", False):
        frames, durs = [], []
        for fr in ImageSequence.Iterator(im):
            durs.append(fr.info.get("duration", 80))
            frames.append(flt.apply(fr, s.tv))
        frames[0].save(s.output, save_all=True, append_images=frames[1:],
                       duration=durs, loop=im.info.get("loop", 0), disposal=2)
    else:
        flt.apply(im, s.tv).save(s.output)
    print("saved", s.output)

if __name__ == "__main__":
    main()
