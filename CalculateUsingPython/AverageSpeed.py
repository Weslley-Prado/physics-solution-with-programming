'''
After driving a car on a straight road for eight kilometers and four hundred meters, you stop for lack of gas.
For the next thirty minutes, you walk another two kilometers along the road until you reach a gas station.
a) What was the total displacement from the start of the trip to the gas station?
'''

print("After driving a car on a straight road for eight kilometers and four hundred meters, you stop for lack of gas.\n"
      "For the next thirty minutes, you walk another two kilometers along the road until you reach a gas station.")

print("\n a) What was the total displacement from the start of the trip to the gas station?")


def calculator_average_speed():
    distanceDriving = input("Write the distance that you drived: ")
    distanceWalking = input("Now, write the distance that you walked: ")
    distanceInitial = input("Now, write the distance initial: ")
    timeInitial = input("What was it time initial? ")
    timeFinal = input("What was it time final? ")

    try:
        float(distanceDriving)
        float(distanceWalking)
        float(distanceInitial)
        float(timeInitial)
        distanceTraveled = (float(distanceDriving) + float(distanceWalking)) - float(distanceInitial)
        print(f'The total distance is {distanceTraveled:.2f}')
        timeTraveled = float(timeFinal) - float(timeInitial)
        averageSpeed = float(distanceTraveled)/timeTraveled
        print(f'This is average speed is {averageSpeed:.2f} m/s')

    except ValueError:
        return False


calculator_average_speed()

