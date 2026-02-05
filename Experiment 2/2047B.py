import math

def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

test_cases = int(input("Enter number of test cases: "))

for _ in range(test_cases):
    length_of_string = int(input("Enter the length of the string: "))
    s = input("Enter the string: ")

    minimum_permutation = float('inf')
    answer = s

    for i in range(length_of_string):
        for j in range(length_of_string):
            temp = list(s)
            temp[i] = temp[j]
            temp = ''.join(temp)

            freq = {}
            for ch in temp:
                freq[ch] = freq.get(ch, 0) + 1

            perm = factorial(length_of_string)
            for f in freq.values():
                perm //= factorial(f)

            if perm < minimum_permutation:
                minimum_permutation = perm
                answer = temp

    print("Result:", answer)