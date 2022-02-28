import re


str = 'Okay cool, My password is 1234 dont tell anyone.'

match = re.search(r'p\w*d is (\w+)\b',str)

if match:
    print(match.group(1))
else:
    print('Nothing')

# h = r"[CHK]h?ann?[aeiu]kk?ah?"

