p = set(range(1,10001))
complement = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    complement.add(i)

check = sorted(p - complement)
for i in check:
    print(i)