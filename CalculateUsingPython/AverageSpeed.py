'''
After driving a car on a straight road for eight kilometers and four hundred meters, you stop for lack of gas.
For the next thirty minutes, you walk another two kilometers along the road until you reach a gas station.
" a) What was the total displacement from the start of the trip to the gas station?"

'''

print("After driving a car on a straight road for eight kilometers and four hundred meters, you stop for lack of gas.\n"
      "For the next thirty minutes, you walk another two kilometers along the road until you reach a gas station.")

print("\n a) What was the total displacement from the start of the trip to the gas station?")

distanceDriving = float(input("Write the distance that you drived: "))
distanceWalking = float(input("Now, write the distance that you walked: "))
distanceInitial = float(input("Now, write the distance initial: "))

distanceTotal = (distanceDriving + distanceWalking) - distanceInitial
print(f'The total distance is {distanceTotal}')