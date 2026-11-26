numbers = [1, 2, 3, 2, 1, 4, 2, 3, 1]
frequency = {}
for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1
for key, value in frequency.items():
    print(f"{key} appears {value} times")

# This Code Time aur Space Complexity
# Time Complexity : o(n)
# Space Complexity : o(k)