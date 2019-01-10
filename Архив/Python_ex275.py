import re


l = 'Красивое лучше, чем уродливое.'

m = re.findall('Красивое', l)

print(m)
