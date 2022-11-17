"""Singly-linked lists."""

from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar('T')  # Generic type variable


class Link(Generic[T]):
    """A link in a singly linked list."""

    head: T
    tail: LList[T]

    def __init__(self, head: T, tail: LList[T]):
        """Prepend a new head to tail."""
        self.head = head
        self.tail = tail

    def __repr__(self) -> str:
        """Representation string."""
        return f'Link({self.head}, {self.tail})'


LList = Optional[Link[T]]  # A list is just a reference to the head or None


new_list = Link(21, Link(43, None))
#print(new_list)

new_list = Link(3, new_list)
#print(new_list)

#print(new_list.tail)



def length(x: LList[T]) -> int:
    """
    Get the length of x.

    >>> length(None)
    0
    >>> length(Link(1, None))
    1
    >>> length(Link(1, Link(2, None)))
    2
    """
    count = 0
    while x != None:
        count += 1
        x = x.tail
    return count
    
#print(length(new_list))

def drop(x: LList[T], k: int) -> LList[T]:
    """
    Drop the first k elements in the list.

    If length(x) < k, return the empty list.

    >>> drop(None, 1) is None
    True
    >>> drop(Link(1, None), 1) is None
    True
    >>> drop(Link(1, Link(2, None)), 1)
    Link(2, None)
    """

    for i in range(k):
        if x == None: 
            return None
        x = x.tail 
    return x 

#print(drop(new_list, 2))
#print(drop(None, 1))
#print(drop(Link(1, None), 1))



def reverse(x: LList[T]) -> LList[T]:
    """
    Reverse a list.

    You decide whether you are allowed to modify the existing list
    or if you want to return a new list and leave the original one
    intact.

    >>> reverse(None) is None
    True
    >>> reverse(Link(1, None))
    Link(1, None)
    >>> reverse(Link(1, Link(2, Link(3, None))))
    Link(3, Link(2, Link(1, None)))
    """
    rev = None 
    while x != None: 
        rev = Link(x.head, rev)
        x = x.tail 
    return rev

#print(reverse(new_list))


def take(x: LList[T], k: int) -> LList[T]:
    """
    Return a list with the first k elements in x.

    If length(x) < k, return the full list. You decide whether you
    want to return a copy of x or the original list.

    >>> take(None, 1) is None
    True
    >>> take(Link(1, None), 1)
    Link(1, None)
    >>> take(Link(1, Link(2, Link(3, None))), 2)
    Link(1, Link(2, None))
    """

    res = None
    while True: 
        if x == None: 
            return res 
        if k == 0:
            return reverse(res)
        x, k, res = x.tail, k-1, Link(x.head, res)
    

#print(new_list)
#print(take(Link(1, Link(2, Link(3, None))), 2))

print(drop(new_list, 2))
print(drop(new_list, 2) ==  Link(43, None))

if Link(43, None) ==  Link(43, None): 
    print(True)