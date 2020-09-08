from typing import *

class TreeNode(object):
    def __init__(self, data: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.data: int = data
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree(object):
    def __init__(self, data):
        self.root: Optional[TreeNode] = None
        self.__constructor(data)

    def __constructor(self, data):
        tuple(map(self.insert, map(TreeNode, data)))

    def data(self):
        return self.root

    def sorted_data(self):
        return list(self.__in_order(self.root))

    def __in_order(self, node):
        if node:
            yield from self.__in_order(node.left)
            yield node.data
            yield from self.__in_order(node.right)

    def insert(self, other: 'TreeNode'):
        if not (next_ := self.root): self.root = other
        else:
            while node := next_:
                if node.data >= other.data:
                    if not (next_ := node.left):
                        node.left = other
                else:
                    if not (next_ := node.right):
                        node.right = other
