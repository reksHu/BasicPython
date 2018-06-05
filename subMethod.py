from class3 import Test3


class SubMethod(Test3):
    def init(self):
        self.blocked = ['SAPM']
test = SubMethod()
test.init()
result = test.filter(['SAPM', 'SPAM', 'SAPM', 'SAPM', 'eggs'])
print(result)

