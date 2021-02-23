# Problem 1
#problem statement:
# Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#given condition:
arr = [10, 15, 3, 7]
k = 17

#my variables:
missing_pair = []

def solution():
    for i in arr:
        if i==k:
            return True
        if i in missing_pair:
            return True
        missing_pair.append(k-i)

print(solution())
