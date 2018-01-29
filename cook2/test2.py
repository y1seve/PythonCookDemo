'''
2.2. Matching Text at the Start or End of a String

'''

filename = 'spam.txt'
print('result1 : ', filename.endswith('.txt'))

print('result2 : ', filename.startswith('file:'))

url = 'http://www.python.org'
print('result3 : ', url.startswith('http:'))

# ====================================================================

import os
filenames = os.listdir('.')
print('filenames : ', filenames)

targetFilenames = [name for name in filenames if name.endswith(('.json', '.txt'))]
print('targetFilenames : ', targetFilenames)

containsTxtfile = any(name.endswith('.txt') for name in filenames)
print('containsTxtfile : ', containsTxtfile)

#=====================================================================
print('result4 : ', filename[-4:] == '.txt')
result5 = url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
print('result5 : ', result5)