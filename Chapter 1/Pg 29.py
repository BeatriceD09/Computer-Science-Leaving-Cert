#1
username = input("Enter your username ")
password = input("Enter your password ")
if (username == "beatrice.dowling@gmail.com") and (password == str(12345)):
    print("Welcome")
    
elif (username != "beatrice.dowling@gmail.com") and (password == str(12345)):
    print("Username is incorrect, try again")
    
elif (username == "beatrice.dowling@gmail.com") and (password != str(12345)):
    print("Password is incorrect, try again")
    
else :
    print("Username and password incorrect, try again")
