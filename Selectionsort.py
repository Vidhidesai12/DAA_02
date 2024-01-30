import random

def selection_sort(array):
    # Selection sort implementation
    for i in range(len(array)):
        current_min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[current_min_index]:
                current_min_index = j
        array[i], array[current_min_index] = array[current_min_index], array[i]
    return array
print("Selection sort")
print("Default it takes random number from 1 to 100 depending on the size of the array you enter")
size= int(input("Enter the size of an array: "))
array=random.sample(range(0,101), size)
print("array Before sort:")
print(array)
sorted_array = selection_sort(array)
print("array After sort:")
print(sorted_array)
