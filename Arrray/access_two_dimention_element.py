
import numpy as np

my_array = np.array([
    [10, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
])

def access_element(array, row_index, col_index) :
    if (row_index <= len(array) and col_index >= len(array[0])) :
        print("Invalid index")
    else :
         print(array[row_index][col_index])

print(access_element(my_array, 1, 2))