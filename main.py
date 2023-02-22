from login import Login
from login import menu
from login import Location

print("__________________________________________________________________________________________")
print("*************welcome to pet selling system*************")
print(" ***This System is only for Buying New Born Pets***")
print("__________________________________________________________________________________________")

print("1.SignUP")
print("2.Login")
while True:
    choice=int(input("Enter your Choice-"))
    if choice==1:
        g=Login()
        g.signin()
        g.login()
        break
    elif choice==2:
        g=Login()
        g.login()
        break
    else:
        print("******Invalid option******")       
lc=menu()
lc.pet()
dd=Location()
dd.area()





