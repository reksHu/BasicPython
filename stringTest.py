
try:
    x = input("enter the first number:")
    y = input("enter the second number:")
    # x = eval(x)
    x = int(x)
    # y = eval(y)
    y = int(y)
    print(x/y)
except ZeroDivisionError as er:
    print(er)

blocked = ['SAPM']
sequence = ['SAPM', 'SPAM', 'SAPM', 'SAPM', 'eggs']
result = [x for x in sequence if x not in blocked]
# print(result)


class MuffledCal:
    __muffled = False
    x = 5




