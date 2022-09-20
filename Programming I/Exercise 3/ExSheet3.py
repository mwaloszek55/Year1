''' Question1:
num1=input("Print input value 1:")
num2=input("Print input value 2:")
num3=input("Print input value 3:")

def sameOrDifferent(num1, num2, num3):
    if num1==num2 and num1==num3:
        return True
    else:
        return False

if sameOrDifferent(num1, num2, num3):
    print("True")
else:
    print("False")

Question 2:
def seasons():
    season=int(input("Enter a number between 1-4: "))
    if season==1:
        print("Winter")
    elif season==2:
        print("Spring")
    elif season==3:
        print("Summer")
    elif season==4:
        print("Autumn")
    else:
        print("Error 404")

seasons()


#Question 3:
import math

def equal_numbers():
    num1=int(input("num1:"))
    num2=int(input("num2:"))
    if num1==num2:
        print(math.sqrt(num1))
    else:
        print(num1 ** num2)

equal_numbers()






#Question 4:
pi=3.14159265359
#print(round(pi, 2))
#print(roundPi)
print(format(3.14159265359, ".2f"))
#roundPi=round(pi, 2)
#print(roundPi * 2)
formatPi=(format(3.14159265359, ".2f"))
print(formatPi * 2)   '''


#question 5:
'''def oddOrEven():
    num1=int(input("number:"))
    if num1%2==0:
        print("even")
    else:
        print("odd")


oddOrEven() '''

#question6:
callMinutes=float(input("minutes of calls: "))
textMessages=float(input("number of text messagesa: "))

def calculateBill(callMinutes, textMessages):

    month=15.0
    print("Base Charge %d" % (month))

    if callMinutes>50.0:
        extraMinutes=callMinutes-50.0
        print(extraMinutes*0.25)

    if textMessages>50.0:
        extraTextMessages=textMessages-50
        print(extraTextMessages*0.25)


    if callMinutes>50.0 or textMessages>50.0:
        tax=0.05*(month+extraTextMessages*0.25+extraMinutes)
        billWithAdds=month + (extraMinutes*0.25) + (extraTextMessages*0.25) + tax
        print("Total Bill Amount:", round(billWithAdds, 2))

    else:
        print("Total Bill Amount %d:" % (month))
        
calculateBill(callMinutes, textMessages)
