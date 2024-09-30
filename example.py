class car:
    def __init__(self, name, age, isowned):
        self.name = name
        self.age = age
        self.isowned = isowned

    def owned(self):
        print("car is " + self.isowned)

class test(car):
    def a(self):
        x = 0

car1 = car("test", "12", "owned")
car1.owned()
