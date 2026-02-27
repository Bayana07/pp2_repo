# n = int(input())
# l = int(input())
# r = int(input())
# li = list(map(int, input().split()))

# start = l-1
# end = r
# res = li[:start] + li[start:end][::-1]+li[end:]
# print(*res)
n = int(input())
# l = input().split()
d = dict()
# un = l[0]
for i in range(n):
    name = input()
    ser = int(input())
    if name in d:
        d[name] += ser
    else:
        d[name] = ser
    
    
for name, total in d.items():
    print(f"{name}: {total}")
    

        
        


