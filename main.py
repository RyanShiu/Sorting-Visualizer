import tkinter as tk
import time
import random

# Global variables
stop_flag = False
data = []  # List to store the dataset
sorting_in_progress = False


def bubble_sort():
    global stop_flag
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                update_canvas()
                time.sleep(0.01)
                if stop_flag:
                    return
        if not swapped:
            break


def selection_sort():
    global stop_flag
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return


def insertion_sort():
    global stop_flag
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return

def merge_sort():
    global stop_flag

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
            update_canvas()
            time.sleep(0.01)
            if stop_flag:
                return

    merge_sort_helper(data, 0, len(data) - 1)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            update_canvas()
            time.sleep(0.01)
            if stop_flag:
                return i

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update_canvas()
    time.sleep(0.01)
    if stop_flag:
        return i + 1

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return


def heap_sort():
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return

def update_canvas():
    canvas.delete("all")
    bar_width = canvas_width / len(data)
    max_height = max(data)
    bar_height_ratio = (canvas_height - 10) / max_height
    for i, height in enumerate(data):
        x1 = i * bar_width
        y1 = canvas_height - height * bar_height_ratio
        x2 = x1 + bar_width
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    canvas.update()


def generate_data():
    global data
    num_elements = num_elements_slider.get()
    data = random.sample(range(1, 101), num_elements)  # Generate a random dataset
    update_canvas()


def start_sorting():
    global stop_flag, sorting_in_progress, data
    if not sorting_in_progress:
        sorting_in_progress = True
        stop_flag = False
        num_elements = num_elements_slider.get()
        data = random.sample(range(1, 101), num_elements)  # Generate a new random dataset
        update_canvas()
        if selected_sort_algorithm.get() == "Bubble Sort":
            bubble_sort()
        elif selected_sort_algorithm.get() == "Selection Sort":
            selection_sort()
        elif selected_sort_algorithm.get() == "Insertion Sort":
            insertion_sort()
        elif selected_sort_algorithm.get() == "Merge Sort":
            merge_sort()
        elif selected_sort_algorithm.get() == "Quick Sort":
            quick_sort(data, 0, len(data) - 1)
        elif selected_sort_algorithm.get() == "Heap Sort":
            heap_sort()
        sorting_in_progress = False


'''def stop_sorting():
    global stop_flag
    stop_flag = True
'''

def update_data_on_algorithm_change(*args):
    global stop_flag, sorting_in_progress
    if sorting_in_progress:
        stop_flag = True
        sorting_in_progress = False



root = tk.Tk()
root.title("Sorting Visualizer")

canvas_width = 800
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

sort_frame = tk.Frame(root)
sort_frame.pack(pady=10)

selected_sort_algorithm = tk.StringVar(value="Bubble Sort")

bubble_sort_button = tk.Radiobutton(sort_frame, text="Bubble Sort", variable=selected_sort_algorithm,
                                   value="Bubble Sort", command=update_data_on_algorithm_change)
bubble_sort_button.pack(side=tk.LEFT, padx=10)

selection_sort_button = tk.Radiobutton(sort_frame, text="Selection Sort", variable=selected_sort_algorithm,
                                      value="Selection Sort", command=update_data_on_algorithm_change)
selection_sort_button.pack(side=tk.LEFT, padx=10)

insertion_sort_button = tk.Radiobutton(sort_frame, text="Insertion Sort", variable=selected_sort_algorithm,
                                      value="Insertion Sort", command=update_data_on_algorithm_change)
insertion_sort_button.pack(side=tk.LEFT, padx=10)

insertion_sort_button = tk.Radiobutton(sort_frame, text="Heap Sort", variable=selected_sort_algorithm,
                                      value="Heap Sort", command=update_data_on_algorithm_change)
insertion_sort_button.pack(side=tk.LEFT, padx=10)

insertion_sort_button = tk.Radiobutton(sort_frame, text="Quick Sort", variable=selected_sort_algorithm,
                                      value="Quick Sort", command=update_data_on_algorithm_change)
insertion_sort_button.pack(side=tk.LEFT, padx=10)

insertion_sort_button = tk.Radiobutton(sort_frame, text="Merge Sort", variable=selected_sort_algorithm,
                                      value="Merge Sort", command=update_data_on_algorithm_change)
insertion_sort_button.pack(side=tk.LEFT, padx=10)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

start_button = tk.Button(control_frame, text="Start", command=start_sorting)
start_button.pack(side=tk.LEFT, padx=10)

num_elements_label = tk.Label(root, text="Number of Elements:")
num_elements_label.pack(pady=10)

num_elements_slider = tk.Scale(root, from_=10, to=100, orient=tk.HORIZONTAL, length=300)
num_elements_slider.set(10)
num_elements_slider.pack()



generate_data()  # Generate initial random data

root.mainloop()

'''


import tkinter as tk
from tkinter import ttk
import random
import time

# Global variables
stop_flag = False
data = []  # List to store the dataset
sorting_in_progress = False


def bubble_sort():
    global stop_flag
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                update_canvas()
                time.sleep(0.01)
                if stop_flag:
                    return
        if not swapped:
            break


def selection_sort():
    global stop_flag
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return


def insertion_sort():
    global stop_flag
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return


def merge_sort():
    global stop_flag

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
            update_canvas()
            time.sleep(0.01)
            if stop_flag:
                return

    merge_sort_helper(data, 0, len(data) - 1)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            update_canvas()
            time.sleep(0.01)
            if stop_flag:
                return i

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update_canvas()
    time.sleep(0.01)
    if stop_flag:
        return i + 1

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return


def heap_sort():
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        update_canvas()
        time.sleep(0.01)
        if stop_flag:
            return


def generate_data():
    global data
    num_elements = num_elements_slider.get()
    data = random.sample(range(1, 101), num_elements)
    update_canvas()


def start_sorting():
    global stop_flag, sorting_in_progress
    if not sorting_in_progress:
        sorting_in_progress = True
        stop_flag = False
        if selected_sort_algorithm.get() == "Bubble Sort":
            bubble_sort()
        elif selected_sort_algorithm.get() == "Selection Sort":
            selection_sort()
        elif selected_sort_algorithm.get() == "Insertion Sort":
            insertion_sort()
        elif selected_sort_algorithm.get() == "Merge Sort":
            merge_sort()
        elif selected_sort_algorithm.get() == "Quick Sort":
            quick_sort(data, 0, len(data) - 1)
        elif selected_sort_algorithm.get() == "Heap Sort":
            heap_sort()
        sorting_in_progress = False


def stop_sorting():
    global stop_flag
    stop_flag = True


def update_canvas():
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    bar_width = canvas_width / len(data)
    bar_height_unit = canvas_height / max(data)
    for i, value in enumerate(data):
        x1 = i * bar_width
        y1 = canvas_height
        x2 = (i + 1) * bar_width
        y2 = canvas_height - (value * bar_height_unit)
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")


def update_data_on_algorithm_change(*args):
    global stop_flag
    if sorting_in_progress:
        stop_flag = True
        start_sorting()
    else:
        update_canvas()


root = tk.Tk()
root.title("Sorting Visualizer")
root.geometry("800x600")
root.resizable(False, False)

main_frame = ttk.Frame(root)
main_frame.pack(pady=20)

canvas = tk.Canvas(main_frame, width=800, height=400, bg="white")
canvas.pack()

sort_frame = ttk.LabelFrame(main_frame, text="Sorting Algorithm")
sort_frame.pack(pady=10)

selected_sort_algorithm = tk.StringVar()
selected_sort_algorithm.set("Bubble Sort")

bubble_sort_button = ttk.Radiobutton(sort_frame, text="Bubble Sort", variable=selected_sort_algorithm,
                                    value="Bubble Sort", command=update_data_on_algorithm_change)
bubble_sort_button.pack(side="left", padx=10)

selection_sort_button = ttk.Radiobutton(sort_frame, text="Selection Sort", variable=selected_sort_algorithm,
                                       value="Selection Sort", command=update_data_on_algorithm_change)
selection_sort_button.pack(side="left", padx=10)

insertion_sort_button = ttk.Radiobutton(sort_frame, text="Insertion Sort", variable=selected_sort_algorithm,
                                       value="Insertion Sort", command=update_data_on_algorithm_change)
insertion_sort_button.pack(side="left", padx=10)

merge_sort_button = ttk.Radiobutton(sort_frame, text="Merge Sort", variable=selected_sort_algorithm,
                                    value="Merge Sort", command=update_data_on_algorithm_change)
merge_sort_button.pack(side="left", padx=10)

quick_sort_button = ttk.Radiobutton(sort_frame, text="Quick Sort", variable=selected_sort_algorithm,
                                    value="Quick Sort", command=update_data_on_algorithm_change)
quick_sort_button.pack(side="left", padx=10)

heap_sort_button = ttk.Radiobutton(sort_frame, text="Heap Sort", variable=selected_sort_algorithm,
                                   value="Heap Sort", command=update_data_on_algorithm_change)
heap_sort_button.pack(side="left", padx=10)

num_elements_label = ttk.Label(main_frame, text="Number of Elements:")
num_elements_label.pack()

num_elements_slider = ttk.Scale(main_frame, from_=10, to=100, orient="horizontal")
num_elements_slider.set(10)
num_elements_slider.pack(pady=10)

generate_data_button = ttk.Button(main_frame, text="Generate Data", command=generate_data)
generate_data_button.pack()

sort_controls_frame = ttk.Frame(main_frame)
sort_controls_frame.pack(pady=20)

start_button = ttk.Button(sort_controls_frame, text="Start", command=start_sorting)
start_button.grid(row=0, column=0, padx=10)

stop_button = ttk.Button(sort_controls_frame, text="Stop", command=stop_sorting)
stop_button.grid(row=0, column=1, padx=10)

root.mainloop()
'''