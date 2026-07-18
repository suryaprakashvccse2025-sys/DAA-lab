import time

comparison_count = 0

def min_max(arr, low, high):
    global comparison_count

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = min_max(arr, low, mid)
    right_min, right_max = min_max(arr, mid + 1, high)

    comparison_count += 1
    minimum = left_min if left_min < right_min else right_min

    comparison_count += 1
    maximum = left_max if left_max > right_max else right_max

    return minimum, maximum

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

start = time.perf_counter()

minimum, maximum = min_max(arr, 0, n - 1)

end = time.perf_counter()

sorted_arr = sorted(arr)

print("\nResults")
print("Minimum :", minimum)
print("Maximum :", maximum)
print("Second Minimum :", sorted_arr[1])
print("Second Maximum :", sorted_arr[-2])
print("Range :", maximum - minimum)
print("Average :", round(sum(arr) / n, 2))
print("Comparisons :", comparison_count)
print("Execution Time : {:.6f} ms".format((end - start) * 1000))