inFile = open("studentFees.txt", 'r') # opens a connection with the file
lines = inFile.readlines()  #reads in the file line by line
newList = []
for word in lines:  #strips & effectively cleans all the unnecessary string
    word = word.replace("\t", " ").strip("\n")
    newList.append(word) #saves all the cleaned string into a new list.


newSplit = []
for i in range(len(newList)): #for loop to seperate the information into lists.
    newSplit.append(newList[i].split(" ")) #splits the information based on spaces and appends it to a new list.

costs = []
names = []
for x in range(len(newSplit)): #for loop to gather the names & costs into a list
    for p in range(0, 1 , 1):
        newSplit[x][p] = newSplit[x][p].lower() #converting first name into lowercase
        newSplit[x][p+1] = newSplit[x][p+1].lower() #converting second name into lowercase
        newSplit[x][p] = newSplit[x][p] + " " #adding a space inbetween first and second name
        names.append(newSplit[x][p]+newSplit[x][p+1]) #putting first and second name together as an element in the list
        costs.append(newSplit[x][p+2])# creating an entry of the fee paid in the list 1 by 1.



names_costs_Dict = {}   #putting both the names list and prices list into a dictionary
for j in range(len(names)):
        names_costs_Dict[names[j]] =  int(costs[j]) #using the names as the key and the integer of the costs as the value.


name_input = input("Enter the name of a student: ") # takes an input from the keyboard
name_inputLower = name_input.lower() #converting the input from the keyboard into lowercase
cost_of_name = names_costs_Dict[name_inputLower] #searching through the dictionary with the key gathered for the keyboard input
print("The fee paid by", name_inputLower, "is:", cost_of_name) #putting everything into a print statement.



totalFees = 0 # accumulator variable
for paid in names_costs_Dict.values():
    totalFees += paid #adds all of the fees paid into 1 variable

print("The total fees paid:", totalFees) #prints all fees paid.

inFile.close()



