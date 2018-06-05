
class InstCt(object):
    count = 0

    def __init__(self):
        InstCt.count += 1

    def __del__(self):
        InstCt.count -= 1

    def howmany(self):
        return InstCt.count


a = InstCt()
b = InstCt()
print(b.howmany())
print(a.howmany())
del b
print(a.howmany())
del a
print(InstCt.count)

