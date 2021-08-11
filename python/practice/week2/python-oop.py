class Customer:
    def __init__(self,name,member_type):
        self.__name = name
        self.member_type = member_type
        print("customer created")
    def getter(self) :
        return self.__name

c = Customer("Caleb","Gold")
print(c.name)
        