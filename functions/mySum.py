def mypow(*paras):
    'caluclate paramiters pow and added as a result'
    result = 0
    for x in paras:
        result+=x**3
    return  result

print(mypow.__doc__)
print(mypow(1,2,3,4,6))