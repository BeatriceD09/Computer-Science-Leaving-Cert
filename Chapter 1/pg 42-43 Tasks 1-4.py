#1
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
    
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1
    
print(numbers)

#2
hours = [12,7,9,9,6,8,2]
total_hours = sum(hours)
print("Total hours spent at home:",total_hours,"hours")

total_liters = total_hours * 0.5
print("Total liters of milk:",total_liters,"L")

cost_per_L = 1 * 1.35
print("Total cost of milk: €",total_cost)'''

#3
rainfall_ = []
for i in range(7):
    rainfall = int(input("Enter amount of rainfall per day: "))
    rainfall_.append(rainfall)
    
total_rainfall = sum(rainfall_)
print("Total amount of rainfall during the week in cm: ",total_rainfall,"cm")
