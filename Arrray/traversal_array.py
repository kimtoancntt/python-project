from array import *

array1 = array('i', [1, 2, 3, 4])

def tranverse_array(array):
    for i in array:
        print(i)

tranverse_array(array1)

# time complexity: O(n)
# space complexity: O(1)