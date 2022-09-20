cData = [[34, 45, 67, 87, 89], [65, 12, 34, 43, 32], [22, 33, 44, 55, 66], [77, 66,55,67, 89], [2, 4, 5,65, 55], [76, 78, 98, 123, 34], [234, 32, 32, 33, 43], [44, 55, 88, 99, 100], [100, 111, 122, 133, 144], [345, 54, 546, 67, 87]]
def busiestCourier (courierData):    
    busiestCourier = None    
    maxDeliveries = 0    
    for courierID in range (len(courierData)):        
        courier = courierData[courierID]        
        mantotal = 0        
        for day in courier:            
            mantotal += day        
            if busiestCourier == None or mantotal > maxDeliveries:
                busiestCourier = courierID            
                maxDeliveries = mantotal    
    return busiestCourier, maxDeliveries
id, deliveries = busiestCourier(cData)
print (id, deliveries)