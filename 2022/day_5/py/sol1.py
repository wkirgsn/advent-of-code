import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint
import re
from copy import deepcopy

with open(Path.cwd().parent / "input.txt", 'r') as f:
    inp_l = [l.strip() for l in f.readlines()]

# part 1
inp_l = inp_l[10:]

stack = ["MJCBFRLH","ZCD", "HJFCNGW", "PJDMTSB", "NCDRJ", "WLDQPJGZ", "PZTFRH", "LVMG", "CBGPFQRJ"]
stack_orig = [list(s) for s in stack]
stack = deepcopy(stack_orig)
print(stack_orig)
for inp in inp_l:
    qty, start, end = [int(s) for s in re.findall(r'\d+', inp)]
    for i in range(qty):
        stack[end-1].append(stack[start-1].pop())

print(''.join([''.join(s)[-1] for s in stack]))

# part 2
print(stack_orig)
stack = deepcopy(stack_orig)
for inp in inp_l:
    qty, start, end = [int(s) for s in re.findall(r'\d+', inp)]
    stack[end-1].extend(stack[start-1][-qty:])
    stack[start-1] = stack[start-1][:-qty]

print(''.join([''.join(s)[-1] for s in stack]))
