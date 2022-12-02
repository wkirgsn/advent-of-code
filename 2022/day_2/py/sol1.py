import numpy as np
import pandas as pd
from pathlib import Path
from pprint import pprint

with open(Path.cwd().parent / "input.txt", 'r') as f:
    inp_l = [l.strip() for l in f.readlines()]

# part 1
strats_l = [i.split(' ') for i in inp_l]
df = pd.DataFrame(strats_l, columns=['opp', 'me'])
CHOSEN_SCORE_MAP = {'X': 1, 'Y': 2, 'Z': 3}
df['scores_1'] = df.me.map(CHOSEN_SCORE_MAP)
score_tab = pd.DataFrame({'A': [3, 6, 0],
                          'B': [0, 3, 6],
                          'C': [6, 0, 3]},
                         index=['X', 'Y', 'Z'])
df['scores_2'] = df.apply(lambda s: score_tab.at[s.me, s.opp], axis=1)
print(df.scores_2.sum() + df.scores_1.sum())


# part 2
df = df.rename(columns={'me': 'desired'})
strat_tab = pd.DataFrame({'A': ['Z', 'X', 'Y'],
                          'B': ['X', 'Y', 'Z'],
                          'C': ['Y', 'Z', 'X']},
                         index=['X', 'Y', 'Z'])

df.scores_2 = df.desired.map({'X': 0, 'Y': 3, 'Z': 6})
df['chosen'] = df.apply(lambda s: strat_tab.at[s.desired, s.opp], axis=1)
df.scores_1 = df.chosen.map(CHOSEN_SCORE_MAP)
print(df.scores_2.sum() + df.scores_1.sum())
