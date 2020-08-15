# def func(*args, **kwargs):
#     print(args[0])
#     print(kwargs["a"])
#
# dic = {"a" : 10, "b": 11, "c": 12}
# func(1,2,3,4, dic)
# '''
# *args 返回元组
# **kwargs 返回字典
# '''


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)






















