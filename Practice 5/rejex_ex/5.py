import re
pattern = r'a.*b'

print(bool(re.fullmatch(pattern, "axxxb")))
print(bool(re.fullmatch(pattern, "ab")))