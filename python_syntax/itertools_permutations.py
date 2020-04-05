"""
HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

from itertools import permutations

string, combination = input().split()

perms = permutations(string, int(combination))
p = sorted(perms)

for i in p:
    print("".join(i))
