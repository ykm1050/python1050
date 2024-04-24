def largest_even_odd(numbers):
    largest_even = -1
    largest_odd = -1
    
    for num in numbers:
        if num % 2 == 0:
            if num > largest_even:
                largest_even = num
        else:
            if num > largest_odd:
                largest_odd = num
    
    return largest_even, largest_odd

numbers = [12, 3, 15, 24, 7, 8, 13, 45, 67, 21, 33, 11, 18]
largest_even, largest_odd = largest_even_odd(numbers)
print("Largest even number: ", largest_even)
print("Largest odd number: ", largest_odd)