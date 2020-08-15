# -*- coding: utf-8 -*


class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None
        self.parent = None


class Tree(object):

    def __init__(self, alist=None):
        self.root = None

        if alist:
            for value in alist:
                self.insert_no_rec(value)

    def insert_rec(self, node, item):

        if not node:
            node = Node(item)
        elif item < node.elem:
            node.lchild = self.insert_rec(node.lchild, item)
            node.lchild.parent = node
        elif item > node.elem:
            node.rchild = self.insert_rec(node.rchild, item)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, item):
        node = self.root

        if not node:
            self.root = Node(item)
            return node

        while True:
            if item < node.elem:
                if node.lchild:
                    node = node.lchild
                else:
                    node.lchild = Node(item)
                    node.lchild.parent = node
                    return node

            elif item > node.elem:
                if node.rchild:
                    node = node.rchild
                else:
                    node.rchild = Node(item)
                    node.rchild.parent = node
                    return node
            else:
                return node

    def query_rec(self, node, item):
        if not node:
            return None
        elif item > node.elem:
            return self.query_rec(node.rchild, item)
        elif item < node.elem:
            return self.query_rec(node.lchild, item)
        else:
            return None

    def query_no_rec(self, item):
        node = self.root

        while node:
            if item > node.elem:
                node = node.rchild
            elif item < node.elem:
                node = node.lchild
            else:
                return node
        return None

    def preorder(self, node):
        if not node:
            return
        print(node.elem, end=",")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def __remove_node_1(self, node):
        # 情况1：node是叶子节点
        if not node.parent:
            self.root = None

        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况2.1：node只有一个左孩子
        if not node.parent:
            self.root = node.lrchild

        if node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent

        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.1：node只有一个右孩子
        if not node.parent:
            self.root = node.rchild

        if node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent

        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, item):
        if self.root:
            node = self.query_no_rec(item)
            if not node:
                return False

            if not node.lchild and not node.rchild:  # 1. 叶子节点
                self.__remove_node_1(node)

            elif not node.rchild:  # 2.1 只有左孩子
                self.__remove_node_21(node)

            elif not node.lchild:  # 2.2 只有右孩子
                self.__remove_node_22()

            else:
                min_node = node.rchild
                while min_node.rchild:
                    min_node = min_node.lchild

                node.elem = min_node.elem
                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


if __name__ == '__main__':
    tree = Tree([4, 6, 7, 9, 2, 1, 3, 5, 8])
    tree.preorder(tree.root)
    print("")
    tree.delete(4)
    tree.preorder(tree.root)
    print("")
    tree.delete(1)
    tree.preorder(tree.root)






















