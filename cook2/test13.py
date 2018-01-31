'''
2.13. Aligning Text Strings

'''

text = 'Hello World'
ltext = text.ljust(20)
print('ltext:', ltext)

rtext = text.rjust(20)
print('rtext:', rtext)

ctext = text.center(20)
print('ctext:', ctext)

# ====================================================

rrtext = text.rjust(20, '=')
print('rrtext:', rrtext)

cctext = text.center(20, '*')
print('cctext:', cctext)

# ====================================================

fltext = format(text, '>20')
print('fltext:', fltext)

frtext = format(text, '<20')
print('frtext:', frtext)

fctext = format(text, '^20')
print('fctext:', fctext)

# ====================================================

text1 = format(text, '=>20s')
print('text1:', text1)

text2 = format(text, '*^20s')
print('text2:', text2)

text3 = format(text, '*<20s')
print('text3:', text3)
