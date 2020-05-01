def test_method(a, b):
    l = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if(a[i]+a[j] == b):
                l.append((a[i], a[j]))
    return l


a = [1,4,45,6,10,-8]
b = 16
t = test_method(a, b)
for i in t:
    print(i)