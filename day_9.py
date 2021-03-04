#Problem 9
#problem statement:
# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

#my variables:
arr1 = [2,4,6,8]
sol1 = 12

arr2 = [5,1,1,5]
sol2 = 10

arr3 = [2,4,6,2,5]
sol3 = 13

arr4 = [6,8,1,7,5,-10,8]
sol4 = 23

arr5 = [-6,-8,-1,-7,-5,-10,-8]
sol5 = 0

def calc_no_adj_sum(arr):
    if (len(arr) == 0):
        return 0
    if (len(arr) == 1):
        return max(arr[0], 0)
    if (len(arr) == 2):
        return max(arr[0], arr[1], 0)

    prev = max(arr[0], 0)
    cur = max(arr[1], arr[0], 0)

    for i in range(2, len(arr)):
        t = max((prev + arr[i]), cur, prev)
        prev = cur
        cur = t
    return max(prev, cur, 0)

def solution():
    assert(calc_no_adj_sum(arr1)==sol1)
    assert(calc_no_adj_sum(arr2)==sol2)
    assert(calc_no_adj_sum(arr3)==sol3)
    assert(calc_no_adj_sum(arr4)==sol4)

solution()