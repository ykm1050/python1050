for i in range(9):
    for j in range(9):
        if i==0 or i==4 or i==8 or j==0:
            print('E',end=' ')
        else:
            print(' ',end=' ')
    print()