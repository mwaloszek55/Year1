'''filename = "debanks.txt"
inFile = open(filename, "r")


line = inFile.readline() # Question 1 a
while line != "":
    line = line.strip()
    print(line)
    line = inFile.readline()



whole = inFile.read()    #Question 1 b
print(whole)
lines = whole.split("\n")
for lineNumber, line in enumerate(lines):
    print(lineNumber, line)



lines = inFile.readlines()
for lineNumber, line in enumerate(lines):
    line = line.strip()
    print(lineNumber, line)

for index, line in enumerate(inFile):
    line = line.strip()
    print(index, line)


inFile.close()'''




'''
filename = "dna.txt"
inFile = open(filename, "r")

whole = inFile.read()
wholesplit = whole.split("\n\n")
for index, dna in enumerate(wholesplit):
    print("%d: %s" % (index, dna))'''




#part1
def readFile(fileHandle):
    clients = []
    clients2 = []
    read = fileHandle.readlines()
    accumulator = 0
    for line in read:
        line = line.strip()
        clients2.append([line])
        clients.append(clients2[accumulator][0].split(", "))
        accumulator+=1
    for ele in clients:
        ele[2] = int(ele[2])
        ele[4] = int(ele[4])
        ele[5] = int(ele[5])
    return clients
#Part 2
def checkMatch (clients):
    i = 0
    for client in clients:
        for client in clients:
            if clients[i][3]==client[1] and client[3]==clients[i][1] and (client[2]>=clients[i][4] or client[2]<=clients[i][5]) and clients[i][0]!=client[0]:
                print(clients[i][0],"could meet",client[0])
        i+=1
        
inFile = open("clients.txt", 'r')
clients = readFile(inFile)
inFile.close()
checkMatch(clients)













