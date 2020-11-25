a = input().split()
b = [x for x in a if x.endswith("s")]
print("_".join(b))
