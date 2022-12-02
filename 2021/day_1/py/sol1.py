import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint

with open(Path.cwd().parent / "input.txt", 'r') as f:
    depth_reads_l = [l.strip() for l in f.readlines()]

depth_reads_mat = np.array(depth_reads_l, dtype=int)
ser = pd.Series(depth_reads_mat)

print(((ser - ser.shift(1)) > 0).astype(int).sum())

sums = ser.rolling(window=3).sum().dropna()

print(((sums[1:] - sums.shift(1).dropna()) > 0).astype(int).sum())

