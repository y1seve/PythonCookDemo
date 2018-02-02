'''
2.15. Interpolating Variables in Strings

'''

s = '{name} has {n} messages.'
text = s.format(name='Guido', n=37)
print('text:', text)

name = 'Guido'
n = 37
text2 = s.format_map(vars())
print('text2:', text2)

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido', 37)
text3 = s.format_map(vars(a))
print('text3:', text3)
# ===========================================================

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
text4 = s.format_map(safesub(vars()))
print('text4:', text4)


# ===========================================================

import sys

def sub(text):
    print('----------', sys._getframe(1).f_locals)
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} message'))
print(sub('Your favourite color is {color}'))


print(sys._getframe(1).f_locals)

