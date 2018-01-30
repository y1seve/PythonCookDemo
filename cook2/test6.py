'''
2.6. Searching and Replacing Case-Insensitive Text

'''

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
targetTexts = re.findall('python', text, flags=re.IGNORECASE)
print('targetTexts:', targetTexts)

text1 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print('text1:', text1)

# ================================================================================
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

text2 = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print('text2:', text2)