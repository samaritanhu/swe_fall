#!/usr/bin/env python
# coding: utf-8
# University of California, Irvine
# Master of Software Engineering, Donald Bren School of Information and Computer Science
# Created by: Xinyi Hu
# Date      : 2020/10/07
# Contact   : xinyih20@uci.edu
# Target    : Realize Linked List by scratch in Python
# Reference : The algorithm design manual


class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.next = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if data is None:
            return None

        node = Node(data)
        if self.head is None:
            self.head = node
            return node

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        return node

    def len(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def print(self):
        print('Linkedlist:', end='')
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print('')
        return

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next
        return


class LinkedListSet:
    def __init__(self):
        self.set = LinkedList()

    def add(self, data):
        if not self.set.search(data):
            self.set.add(data)
            return True
        return False

    def contains(self, data):
        return self.set.search(data)

    def size(self):
        return self.set.len()


if __name__ == "__main__":
    LL = LinkedList()
    LL.print()
    LL.insert(1)
    LL.insert(2)
    LL.print()
    LL.delete(2)
    LL.print()
    print(LL.search(2))
    print(LL.len())