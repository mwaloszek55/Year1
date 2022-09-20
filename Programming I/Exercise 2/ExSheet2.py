'''def howLongToTransmit(distance):
    seconds=distance / 186000 
    return seconds

seconds=round(howLongToTransmit(34000000), 2)
# print(seconds)


def calculateInsurance(replacementCost):
    minimumInsur=replacementCost * 0.8
    print(minimumInsur)

    return minimumInsur

replacementCost=int(input("Input Replacement Cost:"))
calculateInsurance(replacementCost)

def calculatePropertyTax(propertyValue):
    assesmentValue=propertyValue*0.6
    propTax=(assesmentValue/100)*0.64
    return assesmentValue, propTax

print(calculatePropertyTax(100000))'''


A=int(input("How many tickets sold in Class A?:")) * 100
B=int(input("How many tickets sold in Class B?:")) * 80
C=int(input("How many tickets sold in Class C?:")) * 60
D=A+B+C
print("Income generated from ticket sales %d" %(D))