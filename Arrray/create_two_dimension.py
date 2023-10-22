import numpy as np

my_array = np.array([
    [10, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
])

print(my_array)

# Insert new value
newTwoArray = np.insert(my_array, 0, [1, 2, 3, 4], axis=1)
print(newTwoArray)