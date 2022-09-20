'''listOne = [3.14, "John", 45, True]
listTwo = []
#for i in range (4):
#    listTwo.append(type(listOne[counter]))
#    counter+=1
#    print(listTwo)

#for num, name in enumerate(listOne):
#    listTwo.append(num)
#    print(listTwo)

listOne = [3.14, "John", 45, True]
listTwo = []
for i in range(len(listOne)):
    counter=listOne[i]
    index=listOne.index(counter)
    listTwo.append(index)
print(listTwo)

listOne = [114, 32, -8, -32, 9, -85, 110]
listTwo = []
for i in range(len(listOne)):
    if listOne[i]>=0:
        listTwo.append(listOne[i])
print(listTwo)


counties=['Cork', 'Dublin', 'Kerry', 'Waterford']
population=[190384, 1228000, 148717, 49213]
for num, name in enumerate(counties):
    print(name, "has a population of", population[num])'''



counter=int(input("Enter a number: "))
accumulator=1
accumulator2=0
for i in range(counter):
    accumulator2=counter - i
    print(" " * (accumulator2),"*" * (accumulator),sep="")
    accumulator += 2


'''def isStairs(list):
    lenlist=len(list)
    if lenlist<=1:
        result=False
        return result

    comparison=list[0] - list[1]
    if comparison!=1 and comparison!=-1:
        result=False
        return result

    for i in range(lenlist-1):
        step = list[i] - list[i+1] == 1
        if step==comparison:
            result=True
        else:
            result=False
    return result



list1=[8,7,6]
print(isStairs(list1))'''





