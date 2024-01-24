##Running Profile Velocity Acceleration Main File
##Purpose: Take in a CVS File and Calculate:
##Change in Time, Change in Position, Velocity, Time of Velocity, Change in Velocity over an interval, Acceleration, Time of Acceleration

import csv



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

print (new_list)

#scans through each row
for row in new_list:
    category = new_list[row][0]
    distance = new_list[row][1]
    time = new_list[row][2]
    steps = new_list[row][3]


    




