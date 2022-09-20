def binarySearchI(list,data):
	#Algorithm:
	#Keep track of two variables First and Last (index), these are incremented or decremented to limit the part of the 
	#list to be searched. 
	
	#These variables have been created for you and have been iniatialised to the start and end of the list to begin with
	first = 0
	last = len(list) - 1
	found = False

	while found == False:
		#1. Find the middle element of the list using integer division
		mid = (first + last) // 2 #creating a 'mid' variable to hold the index of the middle element of the list.
		#2. If the the middle element/item in the list is equal to the value to be found i.e. data then found is True
		if list[mid] == data: #if statement to check if the 'mid' index of the list is equal to the number we are looking for
			found = True #if the if statement succeeds we have found the number.
		#3. otherwise (code here)
		else:
			#do not change the next two lines of code
			if first == last:		#the entire list has been searched and the number hasn't been found. 
				return False
			#4. Check if the middle element is greater than the value to be found: 
			elif list[mid] > data: #elif statement checking if the 'mid' index of the list is more than the number we need to find.
				#5. Then the element must lie on the first half of the list. Update last index variable
				last = mid #if the statement succeeds we update the 'last' variable to be equal to the 'mid' variable and therefore changing the 'last' index variable
			#6. otherwise 
			else: # if the if statement on line 20 and 23 fails then we execute this.
				#7. then the element must lie on the second half of the list. Update first variable
				first = mid + 1 #this changes the 'first' variable to the 'mid' variable +1, we need to add 1 otherwise the loop never ends.
	return found
	
#result = binarySearchI([2,5,7,8,9,11,14,16],2)		#should return true
#result = binarySearchI([2,5,7,8,9,11,14],2)		#should return true
result = binarySearchI([2,5,7,8,9,11,14,16],15)		#should return false
print (result)