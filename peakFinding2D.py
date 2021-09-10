def max_in_col(arr, rows, col):
    max_value, max_index = 0, 0
    for i in range(rows):
        if max_value < arr[i][col]:
            max_value, max_index = arr[i][col], i
    return max_value, max_index

def find_peak_logic(arr, left_col, right_col):
    rows, cols = len(arr), len(arr[0])
    mid_col = (left_col+right_col) // 2
    max_value, max_index = max_in_col(arr, rows, mid_col)

    if mid_col == 0 or mid_col == cols - 1:
        return max_index, mid_col

    if max_value >= arr[max_index][mid_col+1] and max_value >= arr[max_index][mid_col-1]:
        return max_index, mid_col

    if max_value < arr[max_index][mid_col - 1]:
        return find_peak_logic(arr, left_col, mid_col-1)
    
    if max_value < arr[max_index][mid_col + 1]:
        return find_peak_logic(arr, mid_col+1, left_col)

# Driver for algorithm logic
def find_peak(arr):
    return find_peak_logic(arr, 0, len(arr[0]))

# Driver code
if __name__ == "__main__":
    arr = [ [ 10, 12, 10, 10 ],
            [ 14, 13, 12, 11 ],
            [ 15, 10, 11, 3 ],
            [ 16, 17, 19, 20 ] ]
 
    print(find_peak(arr))
