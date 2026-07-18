import time
import random

def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm
    Time Complexity:
        Best    : O(1)
        Average : O(log log n)
        Worst   : O(n)
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and target >= arr[low] and target <= arr[high]:

        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search Algorithm
    """

    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:

        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


size = int(input("Enter the number of elements: "))

print("Enter the sorted elements:")

arr = list(map(int, input().split()))

target = int(input("Enter the element to search: "))


start = time.perf_counter()

index_is, comp_is = interpolation_search(arr, target)

end = time.perf_counter()

is_time = (end - start) * 1000


start = time.perf_counter()

index_bs, comp_bs = binary_search(arr, target)

end = time.perf_counter()

bs_time = (end - start) * 1000




print("\n========== SEARCH RESULT ==========")

if index_is != -1:
    print(f"Element {target} found at index {index_is}")
else:
    print("Element not found.")

print("\nInterpolation Search")
print("--------------------")
print("Comparisons :", comp_is)
print("Execution Time : {:.6f} ms".format(is_time))

print("\nBinary Search")
print("--------------------")
print("Comparisons :", comp_bs)
print("Execution Time : {:.6f} ms".format(bs_time))


print("\n========== PERFORMANCE ANALYSIS ==========")
print(f'{"Size":>10} {"IS Time(ms)":>15} {"BS Time(ms)":>15} {"IS Comp":>12} {"BS Comp":>12}')
print("-" * 70)

sizes = [1000, 5000, 10000, 50000, 100000]

for s in sizes:

    sample = sorted(random.sample(range(s * 10), s))
    key = sample[random.randint(0, s - 1)]

    start = time.perf_counter()
    idx1, c1 = interpolation_search(sample, key)
    end = time.perf_counter()
    t1 = (end - start) * 1000

    start = time.perf_counter()
    idx2, c2 = binary_search(sample, key)
    end = time.perf_counter()
    t2 = (end - start) * 1000

    print(f'{s:>10} {t1:>15.6f} {t2:>15.6f} {c1:>12} {c2:>12}')