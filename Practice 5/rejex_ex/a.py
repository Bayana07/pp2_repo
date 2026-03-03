import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)