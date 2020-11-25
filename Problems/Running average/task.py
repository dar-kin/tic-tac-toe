a = [int(x) for x in input()]
b = [0 for i in range(len(a) - 1)]
for i in range(len(a) - 1):
    b[i] = float((a[i] + a[i + 1]) / 2)
print(b)
