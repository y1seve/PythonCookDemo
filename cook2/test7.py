'''
2.7. Specifying a Regular Expression for the Shortest Match

'''

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'

texts = str_pat.findall(text1)
print('texts:', texts)

text2 = 'Computer says "no." Phone says "yes."'
text2s = str_pat.findall(text2)
print('text2s:', text2s)

# ========================================================

str_pat_1 = re.compile(r'\"(.*?)\"')
text3s = str_pat_1.findall(text2)
print('text3s:', text3s)