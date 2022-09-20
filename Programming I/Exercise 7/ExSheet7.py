#summation = [8, 9, 10, 11, 12, 13, 14, 15, 16]
#print(summation)

'''def createDeck():    
    suits = ['s', 'h', 'd', 'c']    
    values = ['2', '3', '4','5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']    
    deckOfCards = []    
    for suit in suits:
        for value in values:
            deckOfCards.append([value[0], suit[0]])
    return deckOfCards
deck = createDeck()
print(deck)
print(len(deck))'''



'''def peaks (numList):    
    peaksList = []
    accumulator=1
    if numList != []:
        peaksList.append(numList[0])
    else:
        return peaksList
    for number in range(len(numList)-1):
        if numList[accumulator] > numList[number]:
            peaksList.append(numList[accumulator])
        accumulator+=1
    return peaksList

print(peaks([3, 2, 5, 5, 7, 6, 1, 8, 4])) # #returns [3, 5, 7, 8]
print(peaks([1, 2, 3, 4, 5, 6, 7, 8, 9])) # #returns [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(peaks([9, 8, 7, 6, 5, 4, 3, 2, 1])) # #returns [9]
print(peaks([3])) #returns [3]
print(peaks([])) #returns []'''




cData = [[34, 45, 67, 87, 89], [65, 12, 34, 43, 32], [22, 33, 44, 55, 66,5555], [77, 66,55,67, 89], [2, 4, 5,65, 55], [76, 78, 98, 123, 34], [234, 32, 32, 33, 43], [44, 55, 88, 99, 100], [100, 111, 122, 133, 144], [345, 54, 546, 67, 87]]
def busiestCourier (courierData):    
    busiestCourier = None    
    maxDeliveries = 0
    idss=0
    for ids2 in courierData:
        ids2.append(idss)
        idss+=1
    for ids in courierData:
        for deliveries in ids:
            if maxDeliveries < deliveries:
                maxDeliveries = deliveries
                busiestCourier = ids[-1]
    
            

    return busiestCourier, maxDeliveries
id, deliveries = busiestCourier(cData)
print ("the busiest courier had an ID of %d and had %d deliveries!" % (id, deliveries))













