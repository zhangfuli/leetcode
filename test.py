case = input().strip()
hashmap = {}
res = ''
for i in range(len(case)):
    if case[i] in hashmap:
        hashmap[case[i]] += 1
    else:
        hashmap[case[i]] = 0
        res += case[i]
print(res)