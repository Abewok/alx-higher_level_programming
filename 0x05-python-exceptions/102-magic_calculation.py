#!/usr/bin/python3
def magic_calculation(a, b):
    result1 = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                result1 = result1 + ((a ** b) / i)
        except:
            result1 = a + b
            break
    return result1
