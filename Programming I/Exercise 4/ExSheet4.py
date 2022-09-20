# Question 1
'''userNum=int(input("Enter a number: "))
multiTable=1
while multiTable<=10:
    table=userNum * multiTable
    print(multiTable, "*", userNum, "=", table)
    multiTable += 1'''

# Question 2
'''counter=int(input("Enter a number: "))
def blastOff(counter):
    while counter!=0:
        print(counter)
        counter -= 1
    if counter==0:
        print("Blast off!")
    exit(counter)

blastOff(counter)'''

# Question 3
def bottlesOfBeer():
    numberOfBottles=int(input("Enter the number of bottles: "))
    while numberOfBottles>2:
        numberOfBottlesMinus=numberOfBottles - 1
        print(numberOfBottles,"bottles of beer on the wall,",numberOfBottles, "bottles of beer. Take one down, pass it around, ",numberOfBottlesMinus, "bottles of beer on the wall")
        numberOfBottles-=1
    while numberOfBottles<=2:
        if numberOfBottles==2:
            numberOfBottlesMinus=numberOfBottles - 1
            print(numberOfBottles,"bottles of beer on the wall,",numberOfBottles, "bottles of beer. Take one down, pass it around, ",numberOfBottlesMinus, "bottle of beer on the wall")
            numberOfBottles-=1
        elif numberOfBottles==1:
            numberOfBottlesMinus=numberOfBottles - 1
            print(numberOfBottles,"bottle of beer on the wall,",numberOfBottles, "bottle of beer. Take one down, pass it around, ",numberOfBottlesMinus, "bottles of beer on the wall")
            numberOfBottles-=1
        else:
            quit()

bottlesOfBeer()