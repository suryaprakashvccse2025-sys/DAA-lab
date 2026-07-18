import time

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    i = 0
    j = 0
    comparisons = 0
    positions = []

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions, comparisons


text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

start = time.perf_counter()

positions, comparisons = kmp_search(text, pattern)

end = time.perf_counter()

print("\nSearch Result")

if positions:
    print("Pattern found at positions:", positions)
    print("Total Matches:", len(positions))
else:
    print("Pattern not found")

print("Comparisons:", comparisons)
print("Execution Time: {:.6f} ms".format((end - start) * 1000))

print("\nPerformance Analysis")

print("{:<15}{:<15}{:<20}".format("Text Length", "Comparisons", "Time(ms)"))
print("-" * 50)

for size in [1000, 5000, 10000]:
    sample_text = "A" * (size - 1) + "B"
    sample_pattern = "AB"

    start = time.perf_counter()
    _, comp = kmp_search(sample_text, sample_pattern)
    end = time.perf_counter()

    print("{:<15}{:<15}{:<20.6f}".format(
        size,
        comp,
        (end - start) * 1000
    ))