def elements_n_by_3(arr):
    n = len(arr)
    result = []

    for num in set(arr):
        if arr.count(num) > n // 3:
            result.append(num)

    return result

arr = [3, 2, 3, 2, 2, 1, 3]
print(elements_n_by_3(arr))
