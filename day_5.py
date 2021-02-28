# Problem 5
#problem statement:
# This problem was asked by Jane Street.
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:
# def cons(a, b):
#     return lambda f : f(a, b)
# Implement car and cdr.

#given condition:
def cons(a, b):
    return lambda f : f(a, b)

#my variables:
def car(c):
    f = lambda x,y: x
    return c(f)

def cdr(c):
    f = lambda a,b: b
    return c(f)

def solution():
    print(car(cons(3,5)))
    print(cdr(cons(3,5)))
    pass

solution()