import json
import re


data = '{"Ivan": "123@gmail.com", "Serega": "lol_mail"}'

p = json.loads(data)
for name, em in p.items():
    if re.match(r"\w+@\w+.\w+", em):
        print(name)


# from datetime import datetime, timedelta
# d_str = input()
# n = int(input())
# d = datetime.strptime(d_str, "%Y-%m-%d")
# print((d - timedelta(days=n)).date())


# from datetime import datetime
# st = datetime.strptime(input(), "%Y-%m-%d")
# for _ in range(3):
#     oth = datetime.strptime(input(), "%Y-%m-%d")
#     diff = st - oth
#     print(diff.days)



# n = input()
# gen = sq(10000000)
# for _ in range(n-1):
#     print(next(gen), end=',')
# print(next(gen))
# print(','.join(map(str, sq(n))))

