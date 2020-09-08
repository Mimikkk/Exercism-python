from typing import *

class Node(object):
    def __init__(self, value: int, next_: 'Node' = None):
        self.data = value
        self._next = next_

    def value(self):
        return self.data

    def next(self):
        return self._next


class LinkedList(object):
    def __init__(self, values: Union[List[int], 'LinkedList'] = None):
        self._size = 0
        self._head = None

        for i in (values if values else []): self.push(i)

    def __len__(self) -> int:
        return self._size

    def head(self) -> Node:
        if not self._head: raise EmptyListException("Linked list is empty")
        return self._head

    def push(self, value: int):
        self._size += 1
        new = Node(value, self._head)
        self._head = new

    def pop(self) -> int:
        if not self._head: raise EmptyListException("Linked list is empty")
        value = self._head.value()
        self._head = self._head.next()
        self._size -= 1
        return value

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.pop()
        except EmptyListException:
            raise StopIteration

    def reversed(self) -> 'LinkedList':
        return LinkedList(self)


class EmptyListException(Exception): pass
