import array

my_array = array.array('i', [1, 2, 3, 4])

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(linear_search(my_array, 5))

# time complexity: O(n)
# space complexity: O(1)