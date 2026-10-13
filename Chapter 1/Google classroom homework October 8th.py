# Challenge 1: The Number Hunt

# create a list of random numbers
numbers = [random.randint(1, 99) for i in range(10)]
print(numbers)

# ask user for 3 numbers
user_numbers = []
for i in range(3):
    user_number = int(input("Enter a number:" ))
    user_numbers.append(user_number)

# check if user numbers are on the lit of random numbers
if any(number in numbers for number in user_numbers):
    print("Your number is on the list")

else:
    print("You have not found a number on the list")

# Challenge 2: The Sequential Match
