'''
2.5. Searching and Replacing Text

'''

text = 'yeah, but no, but yeah, but no, but yeah'
text1 = text.replace('yeah', 'yep')
print('text1:', text1)

# ============================================================================

text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
text3 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
print('text3:', text3)

# ============================================================================
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat.sub(change_date, text2)

# ============================================================================
newtext, n = datepat.subn(r'\3-\1-\2', text2)
print('newtext, n:', newtext, n)