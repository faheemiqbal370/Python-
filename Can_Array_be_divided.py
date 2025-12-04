def can_partition(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2

    dp = set([0])

    for num in arr:
        new_dp = set(dp)
        for x in dp:
            if x + num == target:
                return True
            if x + num < target:
                new_dp.add(x + num)
        dp = new_dp

    return False

arr = [1, 5, 11, 5]
print(can_partition(arr))
