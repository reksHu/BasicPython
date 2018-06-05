class ICBC:
    money = 1000000
    branch="default"
    @classmethod
    def totalMoney(cls):
        print("total monmey:",cls.money)

    def __init__(self,branchName):
        self.branch=branchName
        self.money=50000
        self.__class__.money-=50000

    @classmethod
    def printBranchName(self):
        print("brach name:",self.branch)

    def method1(self):
        self.method2()
        pass
    def method2(self):
        pass
ICBC.totalMoney()
i=ICBC('aa')
i.totalMoney()

