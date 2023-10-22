from array import *

my_array = array('i', [1, 2, 3, 4, 5, 6])

def access_array_element(array, index):
    if index >=  len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

access_array_element(my_array, 6)

# time complexity : O(1)
# space complexity: O(1)