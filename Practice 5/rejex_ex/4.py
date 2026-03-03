import re
text = "Hello world Test ABC"

pattern = r'[A-Z][a-z]+'

print(re.findall(pattern, text))