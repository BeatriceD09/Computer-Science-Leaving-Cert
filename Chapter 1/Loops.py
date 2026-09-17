#1
bankBalance = 0
while bankBalance <= 0:
    print("Sorry you have no money in your account")

#2
password = 12345
myPassword = int(input("Enter your password "))
while myPassword != password:
    print("Sorry password is incorrect!")
    break
if myPassword == password:
    print("Welcome!!!")

#2
password = 12345
myPassword = int(input("Enter your password "))
while myPassword != password:
    print("Sorry password is incorrect!")
    myPassword = int(input("Enter your password "))
print("Welcome")
