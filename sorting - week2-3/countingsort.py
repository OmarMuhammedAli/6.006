def counting_sort(a):
    u = max(a) + 1 # max element in the array that dictates the size of the output array
    c = [0] * u # auxiliary array for counting the number of occurrences of each element
    for i in a:
        c[i] += 1 # count the number of occurrences of each element
    for i in range(1, u):
        c[i] += c[i - 1] # add the number of occurrences of each element to the previous element
    b = [0] * len(a) # output array
    for i in a[-1::-1]:
        b[c[i] - 1] = i # put the element in the correct position in the output array
        c[i] -= 1    # update the number of occurrences of the element

    return b

if __name__ == "__main__":
    arr = [1, 4, 1, 2, 7, 5, 2, 4, 3, 2, 1, 4, 1, 7]
    print(counting_sort(arr))