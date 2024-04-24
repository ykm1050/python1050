class A:
    def is_magicalprime(self, num):
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

class B(A):
    def is_neon(self, num):
        num_square = num * num
        return sum(int(digit) for digit in str(num_square)) == num

class C(A):
    def print_name_in_x(self, name):
        length = len(name)
        for i in range(length):
            for j in range(length):
                if i == j or i + j == length - 1:
                    print(name[j], end="")
                else:
                    print(" ", end="")
            print()

class D(A):
    def reverse_string(self, s):
        return s[::-1]

class E(B, C):
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

    def atm_system(self):
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


e = E()
d = D()
e.set_pin(123456)
e.atm_system()
print(e.is_magicalprime(5))
print(e.is_neon(9))
e.print_name_in_x("yuvarajkumar")
s = "r o y a l    c h a l l e n g e r s    b e n g a l u r u"
print(d.reverse_string(s))
