def is_palindrome():
    n = int(input("Enter a number: "))
    s = str(n)
    if s == s[::-1]:
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")
is_palindrome()