# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:37
# @Author  : dengguo
# @File    : binary_tree.py
# @Software: PyCharm

class Node:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.lchild is None:
                    pop_node.lchild = node
                    return
                elif pop_node.rchild is None:
                    pop_node.rchild = node
                    return
                else:
                    q.append(pop_node.lchild)
                    q.append(pop_node.rchild)

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.lchild is not None:
                q.append(pop_node.lchild)
                res.append(pop_node.lchild.item)

            if pop_node.rchild is not None:
                q.append(pop_node.rchild)
                res.append(pop_node.rchild.item)
        return res

    def preorder(self, root):  # 先序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.lchild)
        right_item = self.preorder(root.rchild)
        return result + left_item + right_item

    def inorder(self, root):  # 中序序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.lchild)
        right_item = self.inorder(root.rchild)
        return left_item + result + right_item

    def postorder(self, root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.lchild)
        right_item = self.postorder(root.rchild)
        return left_item + right_item + result


if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    print('层序遍历:', t.traverse())
    print('先序遍历:', t.preorder(t.root))
    print('中序遍历:', t.inorder(t.root))
    print('后序遍历:', t.postorder(t.root))
