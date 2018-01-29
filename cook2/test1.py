'''
2.1. Splitting Strings on Any of Multiple Delimiters

'''
import re
line = 'asdf fjkd; afed, fjek,asdf,    foo'
items = re.split(r'[;,\s]\s*', line)
print('items : ', items)

fields = re.split(r'(;|,|\s)\s*', line)
print('fields : ', fields)

ex_fields = re.split(r'(?:;|,|\s)\s*', line)
print('ex_fields : ', ex_fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print('values : ', values)
print('delimiters : ', delimiters)

results = ''.join(v+d for v,d in zip(values, delimiters))
print('results : ', results)


