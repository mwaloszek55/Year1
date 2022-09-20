'''dictionary1 = {".":1, ",":11, "?":111, "!":1111, ":":11111, "A":2,
 "B":22, "C":222, "D":3, "E":33, "F":333, "G":4, "H":44, "I":444, "J":5, "K":55, "L":555, "M":6, "N":66, "O":666,
  "P":7, "Q":77, "R":777, "S":7777, "T":8, "U":88, "V":888, "W":9, "X":99, "Y":999, "Z":9999,  " ":0}

user_input = input("Enter something:")
for char in user_input:
    char = char.upper()
    print(dictionary1[char], end="")'''











stepData = [[9000, 10000, 10000, 11100, 3400], [2000, 2000, 3400, 5400, 12300], [11000, 12000, 13435, 11234, 10347], [9800, 9500, 8900, 10002, 10054], [4500, 5697,7898, 8796, 10324], [7600, 12000, 12345, 11234, 9820], [13560, 14000, 13000, 11000,10986], [7600, 4356, 9820, 10980, 11240], [10005, 11112, 12243, 13354, 9002], [10340, 10546, 10890, 10002, 9002]]
#(a) The number of week-days on which at least 100,000 steps were made cumulativelyby all employees i.e. Add Columns.
for list1 in stepData:
    steps_together = 0
    for steps in list1:
        steps_together += steps
    if steps_together > 100000:
        numWeekdays =+ 1
numWeekdays = 0

print ("Number of weekdays over 100000: ", numWeekdays) 

#(b) The number of the employee who took the most steps in the week (assume there can only be one). i.e. add the row and check for 
maxemployeeMostStepsID = 0
employeeMostSteps = 0
employeeID = 0

for list1 in stepData:
    steps_together = 0
    for steps in list1:
        steps_together += steps
    if steps_together > employeeMostSteps:
        employeeMostSteps = steps_together
        employeeID = maxemployeeMostStepsID

    maxemployeeMostStepsID += 1


print("Employee ID with most steps: ", employeeID)
