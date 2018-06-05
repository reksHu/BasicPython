def make_exception():
    print('hello')
    raise ValueError
    # raise ValueError('you value Error')
    print('end exception')

# def make_exce2():
#     raise myMessage("value Error")
#
# def myMessage(str):
#     return "error occured,"+str
try:
    make_exception()
except ValueError as ve:
    print(str(ve))
except:
    print("other error")
print("program ended")
