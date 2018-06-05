class Switcher(object):
    def numbers_to_methods_to_strings(self, argument):
        """Dispatch method"""
        # prefix the method_name with 'number_' because method names
        # cannot begin with an integer.
        method_name = 'number_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing")
        # Call the method as we return it
        return method()
    def numbers_to_methodes_dic(self,argument):
        switch ={
            0: self.number_0(),
            1:self.number_1(),
            2:lambda :"two"
        }
        return switch.get(argument,lambda :"nothing")

    def number_0(self):
        return "zero"

    def number_1(self):
        return "one"

    def number_2(self):
        return "two"


s = Switcher()
result = s.numbers_to_methods_to_strings(0)
print(result)
re = s.numbers_to_methodes_dic(3)
print(re)