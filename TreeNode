#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):

  # Implement correct algorithm here

    root = BuildTree(elements)
    if root.InorderTree() == sorted(tree):
        return True
    return False


class BinarySearchTree(object):

    """
    Constructor with vaue we are going  to insert in tree with assigning  left and right child with default None 
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Add_Node(self, data):
        if data == self.data:
            return   # node already exist

        if data < self.data:
            if self.left:
                self.left.Add_Node(data)
            else:
                self.left = BinarySearchTree(data)
        else:

            if self.right:
                self.right.Add_Node(data)
            else:
                self.right = BinarySearchTree(data)

    def Find_Node(self, val):
        """    If current node is equal to  data we are finding return true   """

        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.Find_Node(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.Find_Node(val)
            else:
                return False

    def InorderTraversal(self):
        elements = []
        if self.left:
            elements += selfleft.InorderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.InorderTraversal()

        return elements

    def PostorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.PostorderTraversal()
        if self.right:
            elements += self.right.PostorderTraversal()

        elements.append(self.data)

        return elements

    def PreorderTraversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.PreorderTraversal()
        if self.right:
            elements += self.right.PreorderTraversal()

        return elements

    def Find_Maximum_Node(self):
        if self.right is None:
            return self.data
        return self.right.Find_Maximum_Node()

    def Find_Minimum_Node(self):
        if self.left is None:
            return self.data
        return self.left.Find_Minimum_Node()

    def calculateSumNodes(self):
        left_sum = (self.left.calculateSumNodes() if self.left else 0)
        right_sum = \
            (self.right.calculateSumNodes() if self.right else 0)
        return self.data + left_sum + right_sum


def BuildTree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.Add_Node(elements[i])

    return root


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int,
                    sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print ('CORRECT')
    else:
        print ('INCORRECT')


threading.Thread(target=main).start()
