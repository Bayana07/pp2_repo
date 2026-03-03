import re

pattern = r'ab*'

print(bool(re.fullmatch(pattern, "a")))
print(bool(re.fullmatch(pattern, "abbb")))
print(bool(re.fullmatch(pattern, "ac")))  # False