class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def introduce(self):
        print(f"I'm {self.name} and I'm {self.age} years old.")

child = Child("yuvaraj", 19)

child.greet()
child.introduce()