a = input().lower()
check = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in check:
    if i in a:
        a = a.replace(i, '^')
print(len(a))