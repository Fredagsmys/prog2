""" bst.py

Student:
Mail:
Reviewed by:
Xiaoxia Liu
Date reviewed:
"""

from linked_list import LinkedList
import random
import math
import matplotlib.pyplot as plt


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):  # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):  # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def iter_insert(self, key):
        node = self.root
        if node is None:
            self.root = self.Node(key)
            return self.root

        while node:

            if key < node.key:
                if node.left is None:
                    node.left = self.Node(key)
                else:
                    node = node.left

            elif key > node.key:
                if node.right is None:
                    node.right = self.Node(key)
                else:
                    node = node.right

            else:
                break

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def rec_contains(self, k):
        node = self.root
        if node is None:
            return False

        def _contains(node, k):
            if node is None:
                return False
            if k < node.key:
                return _contains(node.left, k)
            elif k > node.key:
                return _contains(node.right, k)
            else:
                return True

        return _contains(node, k)

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    #
    #   Methods to be completed
    #

    def height(self, ):  # Compulsory
        node = self.root
       # if node is None:
       #     return 0

        def _height(node):
            if node is None:
                return 0
            else:
                return max(1 + _height(node.left), 1 + _height(node.right))

        return _height(node)

    def minNode(self, node):
        # finds the smallest node in the subtree node
        current = node

        # loop down to find the lowest node to the left
        while current.left is not None:
            current = current.left

        return current

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):  # Compulsory
        if r is None:
            return None
        elif k < r.key:

            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)
        elif k > r.key:

            # r.right =  right subtree with k removed
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed

            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.

                # Find the smallest key in the right subtree and make a copy of it
                temp = self.minNode(r.right)

                # Put that key in this node
                r.key = temp.key

                # Remove that key from the right subtree
                r.right = self._remove(r.right, temp.key)

        return r  # Remember this! It applies to some of the cases above

    def __str__(self):  # Compulsory
        if self.size() == 0:
            return '<>'

        lst = '<'
        for node in self:
            print(str(node))
            lst += str(node) + ', '
        lst = lst[0:-2]
        return lst + '>'

    def to_list(self):  # Compulsory
        lst = []
        for node in self:
            lst.append(node)
        return lst

    def to_LinkedList(self):  # Compulsory
        linked = LinkedList()
        for node in self:
            linked.insert(node)

        return linked

    def ipl(self):  # Compulsory

        def _ipl(r, n):
            if r is None:
                return 0
            return n + _ipl(r.left, n + 1) + _ipl(r.right, n + 1)

        return 0 + _ipl(self.root, 1)


def random_tree(n):  # Useful
    t = BST()
    r = random.Random()
    numlist = []
    while t.size() < n:
        number = int(r.random() * 2 * n)

        if number in numlist:
            continue
        else:
            t.insert(number)
            numlist.append(number)

    return t


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)

    # for k in [0, 1, 2, 5, 9]:
    #    print(f"contains({k}): {t.contains(k)}")
    start = 100
    stop = 600
    step = 1
    const = -1.6

    rtrees = []
    ipls = []
    ests = []
    xvals = []

    for n in range(start, stop, step):
        rtree = random_tree(n)
        ipls.append(rtree.ipl() / n)
        ests.append(1.39 * math.log(n, 2))
        xvals.append(n)

    for n in range(start, stop):
        print(ests[(n - start)//step] - ipls[(n - start)//step]) # show that difference stays constant

   #could also show that
    plt.plot(xvals, ipls,'r--', xvals,ests,'g')
    plt.xscale('log')
    plt.show()
    #ipl/n => 1.39 * log2(n) + c


if __name__ == "__main__":
    main()

"""
What is the generator good for?
==============================

1. computing size?
    yes, only wants to find the number of values in tree, not structure-dependent
2. computing height?
3. contains?
    yes equally good, also not structure dependent
4. insert?
5. remove?




Results for ipl of random trees
===============================






"""
