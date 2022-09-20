""" Sample functions for comparing the performance of basic list operations.

"""
import sys
import time


def list_size():
    """ Compare the in-memory sizes of two lists.

    The lists have the same number of objects, but the objects in the second
    list are much bigger.

    The function shows that the in-memory size is determined by the number of
    references, and not by the objects themselves
    """

    mylist = []
    biglist = []
    for i in range(1000):
        mylist.append(1)
        biglist.append((1,2,3,4,5,6,7,8,9,10))
    size = sys.getsizeof(mylist)
    length = len(mylist)
    bigsize = sys.getsizeof(biglist)
    print('List of', length, 'ints occupies', size, 'bytes')
    print('List of', length, 'tuples of of 10 ints occupies', bigsize, 'bytes')

list_size()