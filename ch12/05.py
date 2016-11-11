class Parent:
    house = "yong-san"
    def __init__(self):
        self.money = 10000

class Child1(Parent):
    def __init__(self):
        super().__init__()
        pass

class Child2(Parent):
    def __init__(self):
        pass

child1 = Child1()
child2 = Child2()

print('Child1', dir(child1))
print('Child2', dir(child2))
