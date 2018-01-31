'''
2.14. Combining and Concatenating Strings

'''

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

result1 = ' '.join(parts)

result2 = ','.join(parts)

result3 = ''.join(parts)

print('result1:', result1)
print('result2:', result2)
print('result3:', result3)

a = 'Hello' 'World'
print('a:', a)

# ==============================================================
data = ['ACME', 50, 91.1]
result4 = ','.join(str(d) for d in data)
print('result4:', result4)

# ==============================================================
a = 'a'
b = 'b'
c = 'c'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugl
print(a, b, c, sep=':') # Better


# ==============================================================
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())

with open('test.txt') as f:
    for part in sample():
        f.write(part)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

with open('test.txt') as f:
    for part in combine(sample(), 32768):
        f.write(part)