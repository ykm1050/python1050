def count():
    word = input("Enter a word: ")
    letter = 0
    dig = 0
    punc = 0

    for char in word:
        if char.isalpha():
            letter += 1
        elif char.isdigit():
            dig += 1
        elif char.ispunc():
            punc += 1

    print(f"No of letters: {letter}")
    print(f"No of digits: {dig}")
    print(f"No of puncs: {punc}")
count()