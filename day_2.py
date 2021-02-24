#Problem 2
#problem statement:
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

#given condition:
arr1 = [1,2,3,4,5]
arr2 = [3,2,1]

output1 = [120, 60, 40, 30, 24]
output2 = [2,3,6]

#my variables:
left_traversal = []
right_traversal = []
sol = []

def solution(arr):
    left_traversal.clear()
    right_traversal.clear()
    for i in arr:
        left_traversal.append(1)
        right_traversal.append(1)

    for i in range(0,len(arr),1):
        if(i==0): continue;
        left_traversal[i] = left_traversal[i-1]*arr[i-1]

    for i in range(len(arr)-1,-1,-1):
        if(i==len(arr)-1): continue;
        right_traversal[i] = right_traversal[i+1]*arr[i+1]

    sol.clear()
    for i in range(0, len(arr), 1):
        sol.append(left_traversal[i]*right_traversal[i])




solution(arr1)
assert sol == output1
solution(arr2)
assert sol==output2