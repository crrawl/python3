class Person():
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print(f"Hello, {self.name}")

p = Person('yukurasan')
p.sayHi()