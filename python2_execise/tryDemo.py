def delivaryApp(n):
    print('we have ',n," apples, will delivery to all of you")

    d = int(input("how many peoples :"))
    print("each person will get ",n/d ," apples")

try:
    delivaryApp(10)
except ZeroDivisionError as ex:
    print('error occured,', ex)
except ValueError as ve:
    print("value errored, ",ve)
except:
    print("error occured, but error has been corrected")
else:
    print("else exexuted")
finally:
    print("program exit, quit")