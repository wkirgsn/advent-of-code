import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint

with open(Path.cwd().parent / "input.txt", 'r') as f:
    inp_l = [l.strip() for l in f.readlines()]

# part 1
comps = [(z[:len(z)//2], z[(len(z)//2):]) for z in inp_l]
same_l = [''.join(list(set(list(c1)).intersection(list(c2))))
          for c1, c2 in comps]


def get_value(x):
    if ord(x) <= 96:
        return ord(x) % 64 + 26
    else:
        return ord(x) % 96


vals_l = [[get_value(y) for y in x] for x in same_l]

print(sum(sum(v) for v in vals_l))


# part 2
groups_l = [inp_l[3*i:3*(i+1)] for i in range(len(inp_l) // 3)]
grp_values_l = []
for grp in groups_l:
    grp1, grp2, grp3 = grp
    same = list(set(list(grp1))
                .intersection(set(list(grp2)))
                .intersection(set(list(grp3))))[0]
    grp_values_l.append(get_value(same))
print(sum(grp_values_l))
