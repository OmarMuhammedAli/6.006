def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)

if __name__ == '__main__':
    print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4, 9, -1, 0]))