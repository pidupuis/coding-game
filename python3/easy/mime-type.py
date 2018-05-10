n, q = int(input()), int(input())
ext_to_mt = {ext.lower(): mt for ext, mt in [input().split() for _ in range(n)]}

for _ in range(q):
    fname = input().split(".")
    print(ext_to_mt.get(fname[-1].lower() if len(fname) > 1 else None, "UNKNOWN"))
