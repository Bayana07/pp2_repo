# n = int(input())
# l = int(input())
# r = int(input())
# li = list(map(int, input().split()))

# start = l-1
# end = r
# res = li[:start] + li[start:end][::-1]+li[end:]
# print(*res)
n = int(input())
l = input().split()
d = dict()
un = l[0]
for i in range(n):
    # name = input()
    
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
    
    print(d.values, d.keys)

        
        


