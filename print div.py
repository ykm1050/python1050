def print_5div():
    nums = input("Enter a sequence : ")
    nums_list = nums.split(',')
    div_nums = [int(num, 2) for num in nums_list if int(num, 2) % 5 == 0]
    result = ', '.join(str(num) for num in div_nums)
    print("Nums div by 5:", result)
print_5div()