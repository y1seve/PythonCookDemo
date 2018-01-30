'''
2.8. Writing a Regular Expression for Multiline Patterns Problem

'''

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
            multiline comment */
        '''
text1s = comment.findall(text1)
text2s = comment.findall(text2)

print('text1s:', text1s)
print('text2s:', text2s)


comment1 = re.compile(r'/\*((?:.*|\n)*?)\*/')
text3s = comment1.findall(text2)
print('text3s:', text3s)

# =======================================

comment2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
text4s = comment2.findall(text2)
print('text4s:', text4s)