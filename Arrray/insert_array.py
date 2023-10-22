import array

my_array = array.array('i', [1, 2, 3, 4])
print("Array before insert: ",array)

my_array.insert(0, 6)

print("Array after insert: ", my_array)