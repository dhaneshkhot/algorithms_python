"""
Sample Input

qA2
Sample Output

True
True
True
True
True
"""

str = input()
print(any(c.isalnum() for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))