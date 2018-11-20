# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:38
# @Author  : dengguo
# @File    : binary_sort_tree.py
# @Software: PyCharm
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            self.root = self.insert(self.root, li[0])
            for val in li[1:]:
                self.insert(self.root, val)

    def insert(self, root, val):
        if root is None:
            root = BiTreeNode(val)
        elif val < root.data:
            root.lchild = self.insert(root.lchild, val)
        else:
            root.rchild = self.insert(root.rchild, val)
        return root

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    break
            else:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    break

    def query(self, root, val):
        if not root:
            return False
        if root.data == val:
            return True
        elif root.data > val:
            return self.query(root.lchild, val)
        else:
            return self.query(root.rchild, val)

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data == val:
                return True
            elif p.data > val:
                p = p.lchild
            else:
                p = p.rchild
        return False

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)


tree = BST()
for i in [1, 5, 9, 8, 7, 6, 4, 3, 2]:
    tree.insert_no_rec(i)
tree.in_order(tree.root)
print(tree.query_no_rec(12))
