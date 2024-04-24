def check_pswd(pswd):
    min_len = 6
    max_len = 16
    if max_len < len(pswd) < min_len:
        return False
    if not any(char.isdigit() for char in pswd):
        return False
    if not any(char.islower() for char in pswd):
        return False
    if not any(char.isupper() for char in pswd):
        return False
    special_chars = '$#@'
    if not any(char in special_chars for char in pswd):
        return False
    return True

pswd = input("Enter a password: ")
if check_pswd(pswd):
    print("The password is valid.")
else:
    print("The password is not valid")