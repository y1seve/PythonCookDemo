'''
2.10. Working with Unicode Characters in Regular Expressions

'''

import re
num = re.compile('\d+')

m = num.match('123')

m1 = num.match('\u0661\u0662\u0663')

print('m:', m)
print('m1:', m1)


# ======================================================

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
m2 = pat.match(s)
m3 = pat.match(s.upper())
print('m2:', m2)
print('m3:', m3)
print('s upper:', s.upper())


