class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f"Hello my name is {self.name}")

p1 = Person("Raivis", 18)

print(p1.name)
print(p1.age)
p1.sayHello()
