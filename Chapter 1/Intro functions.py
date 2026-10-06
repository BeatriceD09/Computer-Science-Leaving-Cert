#Challenge 1
#from Challenge 1: here is the speed
def calcSpeed(d,t):
    speed = d/t
    return speed
def checkSpeedLimit(speed):
    limit = 30  # speed limit in m/s
    if speed > limit:
        print("Slow down!")
    else:
        print("Well done!")
#from Challenge 2: here is the marathon time calculation       
def travelTimeEscimator(speed):
    marathon = 42195
    marathon_time = (marathon/speed)/60
    return marathon_time




print("-----Average Speed Calculator-----")

distance = int(input("Enter the distance travelled in meters: "))
time = int(input("Enter the time to complete journey in seconds: "))

#Challenge 1: call up the speed function
average_speed = calcSpeed(distance,time)
print("Average speed = ", round(average_speed, 2), "m")
checkSpeedLimit(average_speed)

#Challenge 2: call up the marathon function
marathon_speed = travelTimeEscimator(average_speed)
print("Time to run marathon in minutes: ", round(marathon_speed, 2), "seconds")


#Challenge 2
'''Challenge 2: Travel Time Estimator
Create a function that uses the calculated avgSpeed to predict how long it would take to travel a much longer distance (like a marathon: 42,195 meters).
Hint: distance divided by speed
Round to 1 dp'''
