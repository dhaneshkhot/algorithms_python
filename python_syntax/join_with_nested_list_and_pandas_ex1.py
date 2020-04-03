# names os second highest scorer
# Input
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''

# output, order alphabetically if more than 1 answers
'''
Berry
Harry
'''

import pandas as pd
import numpy as np

def method1_with_pandas():
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    df = pd.DataFrame(nested_list, columns=['Name', 'Score'])
    sorted_df = df.sort_values(by=['Score', 'Name'])

    lowest_score = sorted_df['Score'].aggregate(np.min)
    result = sorted_df[sorted_df['Score'] > lowest_score].head(2)['Name'].values #not completely right as there could be more than 2

    for i in result:
        print(i)

def method2_without_pandas():
    marksheet = []
    for _ in range(0, int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))

if __name__ == '__main__':
    method2_without_pandas()
