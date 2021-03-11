# Python3 code to demonstrate 
# rotation of list 
# using rotate() 
from collections import deque 

# initializing list 
test_list = [1, 4, 6, 7, 2] 

# printing original list 
print ("Original list : " + str(test_list)) 

# using rotate() to left rotate by 3 
test_list = deque(test_list) 
test_list.rotate(-3) 
test_list = list(test_list) 

# Printing list after left rotate 
print ("List after left rotate by 3 : " + str(test_list)) 

# using rotate() to right rotate by 3 
# back to Original 
test_list = deque(test_list) 
test_list.rotate(3) 
test_list = list(test_list) 

# Printing after right rotate 
print ("List after right rotate by 3(back to original) : "
										+ str(test_list)) 
