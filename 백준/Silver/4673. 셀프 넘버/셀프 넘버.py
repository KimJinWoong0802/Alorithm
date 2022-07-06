all_num = set(range(1,10001))
made_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    made_num.add(i)

self_num = sorted(all_num - made_num)

for i in self_num:
    print(i)