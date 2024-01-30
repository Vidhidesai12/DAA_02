import random

def insertion_sort(array):
    # Insertion sort implementation
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
print("Insertion sort")
print("Default it takes random number from 1 to 100 depending on the size of the array you enter")
size= int(input("Enter the size of an array: "))
array=random.sample(range(0,101), size)
print("array Before sort:")
print(array)
sorted_array = insertion_sort(array)
print("array After sort:")
print(sorted_array)
