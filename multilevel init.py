class Grandparent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Child(Parent):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby

    def introduce(self):
        print(f"I'm {self.name} and I'm {self.age} years old. I love {self.hobby}.")

grandparent = Grandparent("ykm")
parent = Parent("yuvaraj", 40)
child = Child("yuvarajkumar", 19, "RCB")

grandparent.greet()
parent.greet()
child.greet()
child.introduce()