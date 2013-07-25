__author__ = 'Daan Debie'


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def heapify(array, end, i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    largest = i
    if l < end and array[i] < array[l]:
        largest = l
    if r < end and array[largest] < array[r]:
        largest = r
    if largest != i:
        swap(array, i, largest)
        heapify(array, end, largest)


def heap_sort(array):
    end = len(array)
    start = end / 2 - 1
    for i in range(start, -1, -1):
        heapify(array, end, i)
    for i in range(end - 1, 0, -1):
        swap(array, i, 0)
        heapify(array, i, 0)

sqc = [52, 66, 50, 21, 91, 52, 63, 48, 6, 78, 74]
heap_sort(sqc)
print(sqc)