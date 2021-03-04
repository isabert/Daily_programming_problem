#Problem 8
#problem statement:
# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  0   0
#     / \
#    1   0
#   / \
#  1   1

class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def count_unival(head):
    if(head==None):
        is_uni = True
        uval = None
        num = 0
        return is_uni, uval, num
    if(head.left==None and head.right==None):
        is_uni = True
        uval = head.val
        num = 1
        return is_uni,uval,num

    l_is_uni,l_uval,l_num = count_unival(head.left)
    r_is_uni,r_uval,r_num = count_unival(head.right)

    is_uni = False
    uval = None
    num = l_num+r_num
    if (l_is_uni == True and r_is_uni == True and l_uval == r_uval and l_uval == head.val):
        is_uni = True
    if (l_is_uni == True and r_is_uni == True and (
            l_uval == None and head.val == r_uval or r_uval == None and head.val == l_uval)):
        is_uni = True

    if(is_uni==True and l_uval==r_uval):
        uval = l_uval
        num +=1

    if(is_uni==True and l_uval==None and r_uval!=None):
        uval = l_uval
        num +=1

    if(is_uni==True and r_uval==None and l_uval!=None):
        uval = r_uval
        num +=1
    return is_uni, uval, num




def solution():
    head = node(0)
    head.left = node(0)
    head.right = node(0)
    head.right.left = node(1)
    head.right.left.left = node(1)
    head.right.left.right = node(1)
    head.right.right = node(0)
    print(count_unival(head))
solution()
