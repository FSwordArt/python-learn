# -*- coding: utf-8 -*
'''
AVL树的性质：
根的左右子树的高度之差的绝对值不能超过1
根的左右子树都是平衡二叉树
'''

from BST import Node, Tree

class AVLNode(Node):
    def __init__(self, item):
        Node.__init__(self, item)
        self.bf = 0

class AVLTree(Tree):
    def __init__(self, alist=None):
        Tree.__init__(self, alist)

    def rorate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rorate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rorate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c

        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        g.lchild = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0

        return g

    def rorate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p

        g.rhild = p
        p.parent = g

        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else:
            p.bf = 0
            c.bf = 0

        return g

    def insert_no_rec(self, item):
        #1. 和BST一样，先做插入
        p = self.root

        if not p:
            self.root = AVLNode(item)
            return

        while True:
            if item < p.elem:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(item)
                    p.lchild.parent = p
                    node = p.lchild  #node保存的为插入的节点
                    break

            elif item > p.elem:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(item)
                    p.rchild.parent = p
                    node = p.rchild  #node保存的为插入的节点
                    break
            else: #p.elem == item
                return

        #2.更新 balance factor
        while node.parent:
            if node.parent.lchild == node: #传递从左子树来，左子树更沉了
                #更新node.parent的bf -= 1
                if node.parent.bf < 0: #原来node.parent == -1，更新后变成-2
                    #做旋转
                    #看node哪边沉
                    g = node.parent.parent #为了连接旋转之后的子树
                    x = node.parent #旋转前子树的跟
                    if node.bf > 0:
                        n = self.rorate_left_right(node.parent, node)
                    else:
                        n = self.rorate_right(node.parent, node)
                    #记得把n和g连接起来
                elif node.parent.bf > 0:
                    node.parent.bf = 0
                else:
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: #传递从右子树来，右子树更沉了
                #更新node.parent的bf += 1
                if node.parent.bf > 0: #原来node.parent == 1，更新后变成2
                    #做旋转
                    #看node哪边沉
                    g = node.parent.parent
                    x = node.parent  # 旋转前子树的跟
                    if node.bf < 0:
                        n = self.rorate_right_left(node.parent, node)
                    else:
                        n = self.rorate_left(node.parent, node)
                    #记得连接起来

                elif node.parent.bf < 0:
                    node.parent.bf = 0

                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue

            #连接旋转后的子树
            n.parent = g
            if g:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break

            else: #g是根节点
                self.root = n
                break




if __name__ == '__main__':
    tree = AVLTree([9,8,7,6,5,4,3,2,1])
    tree.preorder(tree.root)
    print("")















