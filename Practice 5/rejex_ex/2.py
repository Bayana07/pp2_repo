import re

pattern = r'ab{2,3}'

print(bool(re.fullmatch(pattern, "abb")))
print(bool(re.fullmatch(pattern, "abbb")))
print(bool(re.fullmatch(pattern, "ab")))  # False