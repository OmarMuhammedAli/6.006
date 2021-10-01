def counting_sort(a):
    u = max(a) + 1
    c = [0] * u
    for i in a:
        c[i] += 1
    for i in range(1, u):
        c[i] += c[i - 1]
    b = [0] * len(a)
    for i in a[-1::-1]:
        b[c[i] - 1] = i
        c[i] -= 1

    return b

if __name__ == "__main__":
    arr = [1, 4, 1, 2, 7, 5, 2, 4, 3, 2, 1, 4, 1, 7]
    print(counting_sort(arr))