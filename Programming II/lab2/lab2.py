'''L1 = [5, 8, 1, 9, 7, 3]


#Function definition
def SelectionSort (l):
    #for loop - number of rounds/iterations over the list we need to take
    largestNum = l[0]
    for i in range(len(l)-1):
        #what's my largest number in the list?
        largestNum = max(l[0:len(l)-i])
        #what's my largest number in the list?
        indexLargest = l.index(largestNum)
        #What's the position of this number?#Where am I swapping it to?
        #swap the number at the end of the list to the index where the largest number is
        l[indexLargest] = l[len(l) - (i + 1)]
        #swap the largest number to the 'end' of the list (remember the end is decreasing with each round/pass).
        l[len(l) - (i + 1)] = largestNum
        #so that we can see the output after every round/pass/cycle/iterationreturn l#return the fully sorted list
        #Function invocationmy
        print(l)
    return l
List2 = SelectionSort(L1)'''





def load_data(filename):
    inFile = open(filename, 'r')
    line = inFile.readlines()
    newLine = []
    for line in line:
        line = line.strip().strip("\n").replace(" ", "")
        line = line.split(",")
        newLine.append(line)
    infectionsList = []
    InfectionsDict = {}
    for i in range(len(newLine)):
        infectionsList.append(newLine[i][0])
        newLine[i].remove(newLine[i][0])
    for listNum in newLine:
        for i in range(len(listNum)):
            listNum[i] = int(listNum[i])
    for i in range(len(newLine)):
        InfectionsDict[infectionsList[i]] = newLine[i]
    inFile.close()
    print(InfectionsDict)
    return InfectionsDict


def daily_cases(cumulative):
    new = {}
    for case in cumulative:
        for pos in range(len(cumulative[case])):
            if pos == 0:
                new[case] = [1]
            else:
                occur = cumulative[case]
                diff = occur[pos] - occur[pos-1]
                new[case].append(diff)
    print(new)




InfectionsCum = load_data("lab2/occurences.txt")
daily_cases(InfectionsCum)






