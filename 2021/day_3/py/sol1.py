import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint


with open(Path.cwd().parent / "input.txt", 'r') as f:
    bins_l = [l.strip() for l in f.readlines()]

bins_mat = np.array([[int(b_) for b_ in b] for b in bins_l])
print(np.sum(bins_mat, axis=0))
a = int('0b' +''.join([str(i) for i in ((np.sum(bins_mat, axis=0) > ((len(bins_l) / 2)))).astype(int)]), 2)
print(bin(a), a)
print(bin(~np.uint8(a)), ~np.uint8(a))
c = int(a) * int(~np.uint8(a))
print(c)
