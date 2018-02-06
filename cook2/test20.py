'''
2.20. Performing Text Operations on Byte Strings

'''

data = b'Hello World'

result1 = data[0:5]
print('result1:', result1)

result2 = data.startswith(b'Hello')
print('result2:', result2)

result3 = data.split()
print('result3:', result3)

result4 = data.replace(b'Hello', b'Hello Cruel')
print('result4:', result4)

# ===========================================================

test = bytearray(b'Hello world')
t1 = test[0:5]
print('t1:', t1)

t2 = test.startswith(b'Hello')
print('t2:', t2)

t3 = test.split()
print('t3:', t3)

t4 = test.replace(b'Hello', b'Hello Cruel')
print('t4:', t4)

# ===================================================================

data = b'FOO:BAR,SPAM'
import re
# result5 = re.split('[:,]', data)
result5 = re.split(b'[:,]', data)
print('result5:', result5)

# ==========================================================================
a = 'Hello World'
a1 = a[0]
a2 = a[1]
print(a1, a2, sep=',')

b = b'Hello World'
b1 = b[0]
b2 = b[1]
print(b1, b2, sep=',')

s = b'Hello World'
print(s)
print(s.decode('ascii'))
print(s.decode('utf-8'))



