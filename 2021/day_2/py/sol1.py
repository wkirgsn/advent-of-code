import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint


instr_l = []

with open(Path.cwd().parent / "input.txt", 'r') as f:
    instr_l = [l.strip().split(' ') for l in f.readlines()]

depth, hor = 0, 0
for cmd, i in instr_l:
    if cmd == 'forward':
        hor += int(i)
    elif cmd == 'down':
        depth += int(i)
    elif cmd == 'up':
        depth -= int(i)

print(hor*depth)

depth, hor, aim = 0, 0, 0
for cmd, i in instr_l:
    if cmd == 'forward':
        hor += int(i)
        depth += aim*int(i)
    elif cmd == 'down':
        aim += int(i)
    elif cmd == 'up':
        #depth -= int(i)
        aim -= int(i)

print(hor*depth)