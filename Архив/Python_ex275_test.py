import re


l = 'Красивое лучше, чем уродливое. Красивое2. Красивое3.'

m = re.findall('красивое', l, re.IGNORECASE)

print(m)
