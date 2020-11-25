

n = int(input())
cols = n * 2 - 1

for i in range(n - 1, -1, -1):
    to_print = "#" * (cols - i * 2)
    print(to_print.center(cols))
