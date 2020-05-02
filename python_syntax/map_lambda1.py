"""
s = "dhanesh khot"
l = s.split()

r = map(lambda x: x.title(), l)

print(" ".join(r))

# output = Dhanesh Khot
"""

s = "hello   world  lol"
for x in s.split():
    s = s.replace(x, x.capitalize())
print(s)