##Running Profile Velocity Acceleration Main File
##Purpose: Take in a CVS File and Calculate:
##Change in Time, Change in Position, Velocity, Time of Velocity, Change in Velocity over an interval, Acceleration, Time of Acceleration

import csv
import methods



##create function to pass file through
def load_data(filename):
    #create new list
    myList = []
    #reads csv file
    with open("Lab1.csv", encoding='utf-8-sig') as data:
        numbers_data = csv.reader(data, delimiter=',')

        #skip headers
        next(numbers_data)
        #makes list of lists with row
        for row in numbers_data:
            myList.append(row)
        return myList

#function I created and we pass the readable list through it
new_list = load_data("Lab1.csv")

#assigns each colums to the list instead of one large string
for y in range(len(new_list)):
    new_list[y] = str(new_list[y]).split(",")

#assigning data based on where it is in the table

for x in range(len(new_list)):
    category = new_list[x][0]
    category = category.replace("['", "")
    distance = float(new_list[x][1])
    time = float(new_list[x][2])
    steps = float(new_list[x][3])

    #uses method from methods to do calculations
    v = round(methods.velocity(distance, time), 2)

    #prints each velocity
    print (f"Velocity for {category} is: {v}")




    




