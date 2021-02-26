# Problem 4
#problem statement:
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.
# 0 is not a positive integer.

#SPECIAL STATEMENT:
#THE PROVIDED ANSWER FROM VINEETJOHN IS WRONG
#HERE ARE THE CORRECT SOLUTIONS:
#1.     https://dev.to/nmreddy1911/day-4-finding-the-smallest-positive-missing-integer-from-an-unordered-list-using-python-11a9
#2.     https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
#3.     https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti/51346319#51346319
def missing_int(arr):
    if(len(arr)==0):return 1
    # first, we shall separate arr into a positive part[0,i) and a negative part [i,len(arr))
    low = -1
    high = len(arr)
    pivot = 1

    while(low<high):
        while(low<len(arr)):
            low += 1
            if(low>=len(arr) or arr[low]<pivot): break


        while(high>=0):
            high -= 1
            if(high<0 or arr[high]>=pivot):break

        if(low<high): arr[high],arr[low] = arr[low], arr[high]
    i = low
    for n in arr[0:i]:
        ind = abs(n)
        if(0<ind and ind<=i and arr[ind-1]>=1):
            arr[ind-1]*=-1

    for ind in range(0,i):
        if(arr[ind]>0):
            return ind+1
    return i+1



def solution():
    assert(missing_int([-1,1, 2, 2, 4])==3)
    assert(missing_int([19,-1,7, 5, 2, 3, 4, 1])==6)
    assert(missing_int([3, -2, 4, 1])==2)
    assert(missing_int([])==1)
    assert(missing_int([3, 4, -1, 1])==2)
    assert(missing_int([1, 2, 3])==4)
    assert (missing_int([0]) == 1)


solution()



