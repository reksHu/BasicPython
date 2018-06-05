class Cooker:
    def open_gas(self):
        print("gas opening")
    def close_gas(self):
        print("gas closed")

    def dowork(self):
        print("cooking")

    def __enter__(self):
        self.open_gas()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_gas()
        print("exiting: exc_type=",exc_type,";exc_val=",exc_val,"exc_tb=",exc_tb)
        if(exc_type is None):
            print("existed")
        else:
            print("error occured,",exc_val)


with Cooker() as c:
    # print(3/0)
    c.dowork()



