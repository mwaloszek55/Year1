#filename = "city_day_time.txt"
#inFile = open(filename, "r")
#writeFile = open("city_output.txt", "w")

'''lines = inFile.readlines()

for line in lines:
    lineAppended = line.replace(':', ' ')
    lineAppended2 = lineAppended.replace('\t', ' ')
    writeFile.write(lineAppended2)

inFile.close()
writeFile.close()'''


'''def gen_city_data(fileHandle):
    whole = fileHandle.read()
    wholesplit1 = whole.split("\n")
    wholesplit = [x for x in wholesplit1 if x != ""]
    city_data = []
    for line in wholesplit:
        linesplit = line.split("\t")
        city_data_data = []
        for word in linesplit:
            if ":" in word:
                words = word.split(":")
                for word in words:
                    city_data_data.append(int(word))
            else:
                city_data_data.append(word)
        city_data.append(city_data_data)
    return city_data'''


'''counter = 0
for elements in city_data:
    counter += 1
print(city_data)
print(counter)

counter2 = 0
for elements in city_data:
    if elements[2] == 8:
        if elements[3] == 52:
            counter2 += 1
print(counter2)'''

'''filename = "city_day_time.txt"
inFile = open(filename, "r")
result = gen_city_data(inFile)
print(result)
inFile.close()
#writeFile.close()'''



def analyse (filename):
    frequency = {}
    lettercount = 0
    inputconnection = open(filename, "r")
    lines = inputconnection.readlines()
    for line in lines:
        for character in line:
            if character.isalpha():
                lettercount += 1
                character = character.upper()
                if character in frequency:
                    nigga = frequency[character]
                    frequency.update({character: nigga + 1})
                else:
                    frequency[character] = 1

    '''if letter is already in the dictionary increase value associated with key by 1 other create it in the dictionary. 
    Hint: use the in operator e.g. if item in dictionary 
    ''''''Now that you have created the freq dictionary, print out every key i.e. letter and associated value i.e. number of occurrences'''
    print(frequency)
    inputconnection.close()
file = "story.txt"
analyse(file)
