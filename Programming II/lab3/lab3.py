'''hexToBinaryTable = { '0':'0000', '1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E': '1110','F':'1111' }

def hexToBinary(dictionary, hexString):
    string = ""
    for char in hexString:
        string = string + dictionary[char]
    return string

print(hexToBinary(hexToBinaryTable, 'ABC12'))'''




def senWords(filename):
    inFile = open(filename, 'r')
    sens = inFile.readlines()
    sensNew = []
    for char in sens:
        char = char.strip("\n")
        sensNew.append(char)



    inFile.close()
    return sensNew


def redacting(filename, sens):
    inFile = open(filename, 'r')
    lines = inFile.readline()
    lines = lines.split(" ")
    linesNew = []
    for line in lines:
        line = line.strip("\n")
        linesNew.append(line)
    for word in sens:
        for word2 in linesNew:
            word2 = word2.lower()
            if word in word2:
                index = linesNew.index(word2)
                word2 =  word2.replace(word2, "*" * len(word2))
                linesNew[index] = word2

    inFile.close()
    return linesNew


def redactedFinished(filename, redacted):
    outFile = open(filename, 'w')
    for word in redacted:
        word = word + " "
        outFile.write(word)

    outFile.close()


sensitiveWords = senWords("lab3/sensitiveWords.txt")
redacted = redacting("lab3/unredacted.txt", sensitiveWords)
redactedFinished("lab3/redacted.txt", redacted)


