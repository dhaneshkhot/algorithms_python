"""
input: 1 4 3 2
output: [2, 3, 4, 1]
"""

arr = list(map(int, input().rstrip().split()))
for i in arr[::-1]:
    print(i, end=" ")
