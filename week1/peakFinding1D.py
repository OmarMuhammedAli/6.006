def find_peak_logic(arr, left, right):
    mid = (right + left) // 2
    if len(arr) == 1 or (
        (
            mid == 0 or arr[mid - 1] <= arr[mid]
        ) and (
            mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]
        )
    ):
        return mid

    if arr[mid + 1] > arr[mid]:
        return find_peak_logic(arr, mid+1, right)

    return find_peak_logic(arr, left, mid-1)


# Driver for the algorithm logic
def find_peak(arr):
    return find_peak_logic(arr, 0, len(arr) - 1)


# Driver code
if __name__ == "__main__":

    arr = [1, 0, 4, 5, 1, 20]
    peaks = find_peak(arr)
    print(peaks)
