import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint

with open(Path.cwd().parent / "input.txt", 'r') as f:
    inp_l = [l.strip() for l in f.readlines()]

# part 1
pairs_l = [p.split(',') for p in inp_l]
pairs_l = [(l.split('-'), (r.split('-'))) for l,r in pairs_l]
pairs_l = [(list(range(int(l1),int(l2)+1)), list(range(int(r1),int(r2)+1))) for ((l1, l2), (r1,r2)) in pairs_l]


print(np.array([len(set(l).intersection(set(r))) == len(l) or 
        len(set(l).intersection(set(r))) == len(r) for l,r in pairs_l]).astype(int).sum())


# part 2
print(np.array([len(set(l).intersection(set(r))) > 0 for l,r in pairs_l]).astype(int).sum())