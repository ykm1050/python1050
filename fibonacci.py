def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
print(is_palindrome("racecar")) 
print(is_palindrome("hello")) 
print(is_palindrome("A man a plan a canal Panama"))



def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: multiply n by the factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5)) # 120




def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: multiply n by the factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5)) # 120



def print_divisible_by_five(numbers):
    # Split the input string into a list of strings
    numbers_list = numbers.split(',')

    # Convert each string to an integer and filter out the numbers that are not divisible by 5
    divisible_numbers = [int(num, 2) for num in numbers_list if int(num, 2) % 5 == 0]

    # Join the remaining numbers into a comma-separated string
    result = ', '.join(str(num) for num in divisible_numbers)

    # Print the result
    print(result)

# Example usage
numbers = "1010, 1111, 1001, 1010, 1111, 1001, 1010, 1111, 1001"
print_divisible_by_five(numbers)




def print_5div():
    nums = input("Enter a sequence : ")
    nums_list = nums.split(',')
    div_nums = [int(num, 2) for num in nums_list if int(num, 2) % 5 == 0]
    result = ', '.join(str(num) for num in div_nums)
    print("Nums div by 5:", result)
print_5div()