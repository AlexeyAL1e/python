import re


text = 'Привидение прошуршало и исчезло в углу.'

m = re.findall('.ло', text)

print(m)
