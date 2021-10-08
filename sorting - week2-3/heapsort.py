def max_heapify(array, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and array[left] > array[i]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

def build_max_heap(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        max_heapify(array, len(array), i)

def heapsort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heapify(array, i, 0)


if __name__ == "__main__":
    array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 6, 0, -1]
    heapsort(array)
    print(array)