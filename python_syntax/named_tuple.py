# input
'''
5
ID	MARKS	NAME	CLASS
1	97	a	7
2	50	b	4
3	91	c	9
4	72	d	5
5	79	e	6
'''

# output --> 77.80
from collections import namedtuple

(n, categories) = (int(input()), input().split())
Student = namedtuple('Student', categories)
marks = [int(Student._make(input().split()).MARKS) for _ in range(n)]
print(format((sum(marks) / len(marks)), '.2f'))