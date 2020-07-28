# Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 

import functools
import operator

def convert_to_str(n):
    return str(n)
sample =  [[1,2,3],[4,5],[6,7,8]]

result = functools.reduce(operator.iconcat, sample, [])

result = list(map(convert_to_str, result))

result = functools.reduce(operator.iconcat, result, '')

print(result)
