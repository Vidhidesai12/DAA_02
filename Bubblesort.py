import random

def bubble_sort(array):
    # Bubble sort implementation
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
print("Bubble sort")
print("Default it takes random number from 1 to 100 depending on the size of the array you enter")
size= int(input("Enter the size of an array: "))
array=random.sample(range(0,101), size)
print("array Before sort:")
print(array)
sorted_array = bubble_sort(array)
print("array After sort:")
print(sorted_array)
