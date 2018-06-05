def myyield():
    yield 1
    yield 7

def yield2():
    l = range(1,10,2)
    for x in l:
        yield x

def testYield2():
    it = yield2()
    try:
        while True:
            print(next(it))
    except StopIteration as ex:
        print("ended")

def testMyyield():
    it = myyield()
    try:
        while True:
            print(next(it))
    except StopIteration as ex:
        print("ended")

testYield2()


