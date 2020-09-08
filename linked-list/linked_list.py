from typing import *

class Node(object):
    def __init__(self, value = None, next_: 'Node' = None, prev: 'Node' = None):
        self.value = value
        self.next = next_
        self.prev = prev

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node(next_=self.head)
        self.__len: int = 0

        self.head.prev = self.tail

    def __iter__(self):
        cursor = self.head.prev
        while cursor != self.tail:
            yield cursor.value
            cursor = cursor.prev

    def __len__(self):
        return self.__len

    def push(self, value):
        new_node = Node(value, next_=self.tail.next, prev=self.tail)
        self.tail.next.prev = new_node
        self.tail.next = new_node
        self.__len += 1

    def pop(self):
        if (temp := self.tail.next).value is None: raise ValueError('List is Empty')

        self.tail.next = temp.next
        self.tail.next.prev = self.tail
        self.__len -= 1

        return temp.value

    def unshift(self, value):
        new_node = Node(value, next_=self.head, prev=self.head.prev)
        self.head.prev.next = new_node
        self.head.prev = new_node
        self.__len += 1

    def shift(self):
        if (temp := self.head.prev).value is None: raise ValueError('List is Empty')

        self.head.prev = temp.prev
        self.head.prev.next = self.head
        self.__len -= 1

        return temp.value
