'''
2.11. Stripping Unwanted Characters from Strings

'''

s = ' hello world \n'

s1 = s.strip()
print('s1:', s1)

s2 = s.lstrip()
print('s2:', s2)

s3 = s.rstrip()
print('s3:', s3)

# ===================================

t = '-----hello====='
t1 = t.lstrip('-')
t2 = t.strip('=-')
print('t1:', t1)
print('t2:', t2)

# ===================================
p =  ' hello        world \n'
p1 = p.strip()
print('p1:', p1)

p2 = p.replace(' ', '')
print('p2:', p2)

import re
p3 = re.sub('\s+', ' ', p)
print('p3:', p3)


# ========================================================
with open('filename.txt') as f:
    lines = (line.strip for line in f)
    for line in lines:
        pass
