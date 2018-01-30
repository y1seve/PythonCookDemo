s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print('s1:', s1)
print('s2:', s2)

print('s1 == s2 ?', s1 == s2)
print('len(s1):', len(s1))
print('len(s2):', len(s2))
# ========================================================

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print('t1 == t2 ?', t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print('t3 == t4 ?', t3 == t4)
print(ascii(t3))

# ========================================================
m1 = unicodedata.normalize('NFD', s1)
m2 = ''.join(c for c in m1 if not unicodedata.combining(c))
print('m2:', m2)