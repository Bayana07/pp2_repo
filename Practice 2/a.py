n = int(input())
d = {}
cnt = 0
for i in range(n):
    s, cnt = input().split()
    cnt = int(cnt)
    if s in d:
        d[s] += cnt
    else:
        d[s] = cnt
for k in sorted(d):
    print(k, d[k])
#     if s in l:
#         l[s] += 1
#     else:
#         l[s] = 1
# for k in l:
#     if l[k] == 3:
#         cnt += 1
# print(cnt)
