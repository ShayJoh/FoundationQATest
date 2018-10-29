'''
Return unique values from a defined list

i.e. input: [1,1,2,3,4,2,4,3,5]
Output: [5]

Input: [1,2,2,3,4,4,3,5]
Output: [1,5]
'''

# Import Collections library
import collections

# Define lists
l1 = [1,2,2,3,3,4,4,5]
l2 = [1,1,1,2,3,3,4,5,5,6,7,7]

# Display the numbers on the screen if the 
# amount of times they appear in collections.Counter(a).items() is equal to 1
# ie, print only the numbers that have no duplicates.

uniq = [item for item, count in collections.Counter(l2).items() if count == 1]

print("The following values are unique: ", uniq)
