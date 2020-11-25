a = input().split()
a = [int(x) for x in a]
x = int(input())
count = 0
for i in range(len(a)):
    if a[i] == x:
        count += 1
        print(i, end=" ")
if count == 0:
    print("not found")
