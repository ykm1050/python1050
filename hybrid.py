class Parent:
    def is_magical_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

class A(Parent):
    def is_neon(self, num):
        num_square = num * num
        return sum(int(digit) for digit in str(num_square)) == num

class B(Parent):
    def print_name_in_x(self, name):
        length = len(name)
        for i in range(length):
            for j in range(length):
                if i == j or i + j == length - 1:
                    print(name[j], end="")
                else:
                    print(" ", end="")
            print()

class C(Parent):
    def reverse_string(self, s):
        return s[::-1]

class D(A, B):
    def __init__(self):
        self.pin = None
        self.balance = 0

    def set_pin(self, pin):
        self.pin = pin

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return "Amount withdrawn successfully"

d = D()
c = C()
d.set_pin(1234)
d.deposit(1000)
print(d.withdraw(500))
print(d.get_balance())
print(d.is_magical_prime(5))
print(d.is_neon(9))
d.print_name_in_x("yuvaraj")
s = "royal challengers bengaluru"
print(c.reverse_string(s))