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
        print(f"Amount deposited successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        print(f"Amount withdrawn successfully. New balance: {self.balance}")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def is_valid_pin(self, pin):
        return self.pin == pin

    def interactive_atm(self):
        print("Welcome to the ATM!")
        pin = int(input("Please enter your PIN: "))
        if not self.is_valid_pin(pin):
            print("Invalid PIN. Exiting...")
            return
        while True:
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Exit")
            option = int(input("Enter your choice: "))
            if option == 1:
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif option == 2:
                amount = float(input("Enter the amount to withdraw: "))
                result = self.withdraw(amount)
                if result == "Insufficient balance":
                    print(result)
            elif option == 3:
                self.check_balance()
            elif option == 4:
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Example usage
d = D()
c = C()
d.set_pin(1234)
d.interactive_atm()
print(d.is_magical_prime(5))
print(d.is_neon(9))
d.print_name_in_x("yuvaraj")
s = "royal challengers bengaluru"
print(c.reverse_string(s))