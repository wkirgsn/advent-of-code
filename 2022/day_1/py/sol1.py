import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint


calorie_l = []

with open(Path.cwd().parent / "input.txt", 'r') as f:
    calorie_l = [l.strip() for l in f.readlines()]

elves_rations = [[]]
for cal in calorie_l:
    if cal == '':
        elves_rations.append([])
    else:
        elves_rations[-1].append(int(cal))

elves_sum_of_cal = [sum(items) for items in elves_rations]

print(elves_sum_of_cal)

print(max(elves_sum_of_cal))

print(np.sort(elves_sum_of_cal)[:3].sum())
