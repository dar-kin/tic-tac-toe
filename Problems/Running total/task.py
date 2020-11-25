
a = [int(x) for x in input()]
for i in range(1, len(a)):
    a[i] += a[i - 1]
print(a)
