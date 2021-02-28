#Problem 6
#problem statement:
# This problem was asked by Google.
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

#my variables:
next_pointer_address=88
system = {}
def get_pointer():
    #sudo get pointer
    global next_pointer_address
    next_pointer_address +=4
    return next_pointer_address-4

class node:
    def __init__(self,val,pointers):
        global system
        self.val =val
        self.current_ptr=get_pointer()
        self.pointers = pointers
        system[self.current_ptr] = self

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.headptr = None
        self.tailptr = None
        self.length = 0

    def add(self,val):
        t = node(val,self.tailptr)
        t_ptr = t.current_ptr
        self.length +=1
        if(self.head==None):
            self.head = t
            self.headptr = t_ptr
        elif(self.head!=None and self.tail==None):
            t.pointers = self.headptr
            self.head.pointers = t_ptr
            self.tail = t
            self.tailptr = t_ptr

        else:
            self.tail.pointers ^= t_ptr
            self.tail = t
            self.tailptr = t_ptr

    def get(self,index):
        if(index>=self.length):return None;
        #assume zero based
        prev_ptr = None
        cur_ptr = self.headptr
        i=0
        while(i<=index):
            n  =system[cur_ptr]
            if(i==index):
                return n.val
            if(i<index):
                i+=1
                next_ptr = None
                if(i==1):
                    next_ptr = n.pointers
                else:
                    next_ptr = n.pointers^prev_ptr

                prev_ptr = cur_ptr
                cur_ptr = next_ptr



def solution():
    # a = get_pointer()
    # print(a)
    # print(bin(a))
    # print(int(bin(a),2))
    # print(a^(a+12))

    ll = linkedlist()
    ll.add('a')
    ll.add('b')
    ll.add('c')
    ll.add('d')
    ll.add('e')
    ll.add('f')
    ll.add('g')

    global system
    for key in system:
        print("{}: val={} current_pointer={} pointers={}".format(key, system[key].val, system[key].current_ptr, system[key].pointers))

    print(ll.get(0))
    print(ll.get(1))
    print(ll.get(2))
    print(ll.get(3))
    print(ll.get(4))
    print(ll.get(5))
    print(ll.get(6))
    print(ll.get(7))
    print(ll.get(8))


solution()