'''
2.3. Matching Strings Using Shell Wildcard Patterns

'''
from fnmatch import fnmatch, fnmatchcase

result1 = fnmatch('foo.txt', '*.txt')
print('result1 :', result1)

result2 = fnmatch('foo.txt', '?oo.txt')
print('result2 :', result2)

result3 = fnmatch('Dat45.csv', 'Dat[0-9]*')
print('result3:', result3)

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
targetNames = [name for name in names if fnmatch(name, 'Dat*.csv')]
print('targetNames:', targetNames)

# ==========================================================

result4 = fnmatchcase('foo.txt', '*.TXT')
print('result4:', result4)


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

targetAddr1 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print('targetAddr1:', targetAddr1)

targetAddr2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print('targetAddr2:', targetAddr2)
