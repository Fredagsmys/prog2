""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""
import time


class LinkedList:
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):  # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):  # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):  # Optional
        f = self.first
        counter = 0
        while f:
            counter += 1
            f = f.succ
        return counter

    def mean(self):  # Optional
        f = self.first
        sum = 0
        len = self.length()
        while f:
            sum += f.data
            f = f.succ
        return sum / len

    def remove_last(self):  # Optional

        f = self.first
        if f is None:
            return None

        if self.length() == 1:
            last = self.first
            self.first = None
            return last.data

        for _ in range(self.length() - 2):
            f = f.succ
        last = f.succ
        f.succ = None
        return last.data

    def remove(self, x):  # Compulsory
        f = self.first
        if f is None or x < f.data:
            return False
        if f.data == x:
            return True
        while f.succ:
            if x == f.succ.data:
                f.succ = f.succ.succ
                return True
            else:
                f = f.succ

        return False

    def count(self, x):  # Optional

        def _count(f, x):
            if f is None:
                return 0
            elif f.data == x:
                return 1 + _count(f.succ, x)
            else:
                return 0 + _count(f.succ, x)

        return _count(self.first, x)

    def to_list(self):  # Compulsory

        def _to_list(f):
            if f is None:
                return []
            else:
                return [f.data] + _to_list(f.succ)

        return _to_list(self.first)

    def remove_all(self, x):  # Compulsory
        def _remove_all(f, x):
            if f is None:
                return 0

            if self.length() == 1:
                if f.data == x:
                    self.first = None
                    return 1

            if f.data == x and self.first == f:
                self.first = f.succ
                return 1 + _remove_all(self.first,x)

            if f.succ is None:
                return 0

            elif f.succ.data == x:
                f.succ = f.succ.succ
                return 1 + _remove_all(f, x)

            else:
                return 0 + _remove_all(f.succ, x)

        return _remove_all(self.first, x)

    def __str__(self):  # Compulsary
        if self.first == None:
            return '()'

        lst = '('
        for f in self:
            lst += str(f)
            lst += ', '
        lst = lst[0:-2]
        lst += ')'
        return lst

    def copy(self):  # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result

    ''' Complexity for this implementation: 
        O(n^2)
        t(n) = c*n^2
        time scales quadraticaly with size of the list that is being copied.
        In each for iteration, the insert function is called.
        Because the list is sorted, the insert function will have to iterate through the entire list every time.
    '''

    def myCopy(self):  # Compulsary
        result = LinkedList()
        f = self.first
        if f:
            result.first = result.Node(f.data, f.succ)
        #else:
            #return result
        g = result.first
        while f.succ:
            g.succ = result.Node(f.succ.data, None)
            f = f.succ
            g = g.succ
        return result

    ''' Complexity for this implementation:
        O(n)
        t(n) = c*n 
        time scales linearly with size of list being copied.
    '''

    def __getitem__(self, ind):  # Compulsory
        f = self.first
        for _ in range(ind):
            f = f.succ
            if f is None:
                raise IndexError
        return f.data


class Person:  # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self, other):
        self_mag = self.pnr
        other_mag = other.pnr
        return self_mag < other_mag

    def __le__(self, other):
        self_mag = self.pnr
        other_mag = other.pnr
        return self_mag <= other_mag

    def __eq__(self, other):
        self_mag = self.pnr
        other_mag = other.pnr
        return self_mag == other_mag

    def __ne__(self, other):
        self_mag = self.pnr
        other_mag = other.pnr
        return ~(self_mag == other_mag)

    def __gt__(self, other):
        self_mag = self.pnr
        other_mag = other.pnr
        return self_mag > other_mag

    def __ge__(self, other):
        self_mag = self.pnr
        other_mag = other.pnr
        return self_mag >= other_mag


def main():

    lst = LinkedList()
    for x in [3, 1, 2, 6, 1]:
        lst.insert(x)
    lst.print()
    lst.remove_all(3)
    lst.print()
    lst.remove_all(2)
    lst.print()
    lst.remove_all(1)
    lst.print()
    lst.remove_all(6)
    lst.print()

if __name__ == '__main__':
    main()
