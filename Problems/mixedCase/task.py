a = input().split()
a[0] = a[0].lower()
for i in range(1, len(a)):
    a[i] = a[i].capitalize()
print("".join(a))
