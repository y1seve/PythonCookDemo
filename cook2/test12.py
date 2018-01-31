'''
2.12. Sanitizing and Cleaning Up Text

'''

s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None
}

a = s.translate(remap)
print('a:', a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                        if unicodedata.combining(chr(c)))
                    
b = unicodedata.normalize('NFD', a)
print('b:', b)

c = b.translate(cmb_chrs)
print('c:', c)


# ================================================

digitmap = { c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd' }
print(len(digitmap))

x = '\u0661\u0662\u0663'
x1 = x.translate(digitmap)
print('x1:', x1)

# ================================================

n1 = 'pýtĥöñ is awesome\n'
n2 = unicodedata.normalize('NFD', a)
print('n2:', n2)
n3 = n2.encode('ascii', 'ignore').decode('ascii')
print('n3:', n3)


