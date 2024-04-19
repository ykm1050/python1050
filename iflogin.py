email="bala@gmail.com"
pwd=123456
uemail=str(input("Enter the email"))
upwd=int(input("Enter the pwd"))
if(email == uemail and pwd==upwd):
    print("login success")
else:
    print("login failed")