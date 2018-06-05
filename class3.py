class Test3:
    # def __init__(self, age):
    #     self.val = 10
    #     self.age = age

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        print(sequence)
        return [x for x in sequence if x not in self.blocked]





