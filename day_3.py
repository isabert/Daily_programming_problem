#Problem 3
#problem statement:
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

#given condition:
#None

#my variables:
#None
import json

class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree2string(root):
    if(root==None): return None;
    jsond = {}
    jsond['val'] = root.val
    l_tree = tree2string(root.left)
    r_tree = tree2string(root.right)

    jsond['left'] = l_tree
    jsond['right'] = r_tree
    return jsond

def string2tree(d):
    if(d==None): return None;
    root = node(d['val'])
    root.left = string2tree(d['left'])
    root.right = string2tree(d['right'])
    return root;


def solution():
    #contruct the tree
    root = node('a')
    root.left = node('b')
    root.right = node('c')
    root.left.left = node('d')
    root.left.right = node('g')
    root.right.left = node('h')
    root.right.right = node('k')
    root.left.left.right = node('e')
    root.left.left.right.left = node('f')
    root.right.left.left = node('i')
    root.right.left.right = node('j')

    #tree serialization
    json_dict = tree2string(root=root)
    jsons = json.dumps(json_dict)
    jsons_pretty = json.dumps(json_dict, indent =4)
    print(jsons_pretty)

    #tree deserialization
    json_dict = json.loads(jsons)#cannot do indent??
    root  = string2tree(json_dict)


solution()