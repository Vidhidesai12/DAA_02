import time
import matplotlib.pyplot as plt
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

def selection_sort(array):
    # Selection sort implementation
    for i in range(len(array)):
        current_min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[current_min_index]:
                current_min_index = j
        array[i], array[current_min_index] = array[current_min_index], array[i]

def bubble_sort(array):
    # Bubble sort implementation
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def generate_data(size):
    return random.sample(range(size * 10), size)

def benchmark_sorting_algorithm(sorting_function, input):
    array = generate_data(input)
    
    start_time = time.time()
    sorting_function(array)
    end_time = time.time()
    
    return end_time - start_time

input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000]  # Add more as needed
sorting_algorithms = [insertion_sort, selection_sort, bubble_sort]
algorithm_names = ["Insertion Sort", "Selection Sort", "Bubble Sort"]

for i, sorting_function in enumerate(sorting_algorithms):
    times = [benchmark_sorting_algorithm(sorting_function, size) for size in input_sizes]

    # Plotting
    plt.plot(input_sizes, times, label=algorithm_names[i])

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
