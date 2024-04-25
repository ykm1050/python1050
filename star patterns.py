def print_star_pattern(n):
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

print_star_pattern(5)