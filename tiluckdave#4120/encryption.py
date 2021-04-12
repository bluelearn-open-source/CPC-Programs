import math

def encryption(s):
    str1 = ''
    count = len(s)
    sqrt  = math.ceil(math.sqrt(count))
    for j in range(sqrt):
        for index, i in enumerate(s):
            if index%(sqrt) == j:
                str1 += i
        str1 += ' '
    return str1
