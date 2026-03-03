import re

text = "hello_world test_value notMatch"

pattern = r'[a-z]+_[a-z]+'

print(re.findall(pattern, text))