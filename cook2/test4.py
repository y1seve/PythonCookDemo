'''
2.4. Matching and Searching for Text Patterns

'''

text = 'yeah, but no, but yeah, but no, but yeah'
index = text.find('no')
print('index:', index)

# =========================================================

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# ==============================================================
text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text3List = datepat.findall(text3)
print('text3List:', text3List)

# ==============================================================
datepat_g = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat_g.match('11/27/2012')
print('m:', m)

# Extract the contens of each group
content0 = m.group(0)
print('content0:', content0)

content1 = m.group(1)
print('content1:', content1)

content2 = m.group(2)
print('content2:', content2)

content3 = m.group(3)
print('content3:', content3)

contents = m.groups()
print('contents:', contents)

month, day, year = contents
print('{}/{}/{}'.format(month, day, year))

text4 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
matches = datepat_g.findall(text4)
print('matches:', matches)

for m in datepat_g.finditer(text4):
    print('m:', m.groups())

# ==============================================================

datepat_s = re.compile(r'(\d+)/(\d+)/(\d+)$')
m1 = datepat_s.match('11/27/2012abcdef')
m2 = datepat_s.match('11/27/2012')
print('m1, m2', m1, m2)
