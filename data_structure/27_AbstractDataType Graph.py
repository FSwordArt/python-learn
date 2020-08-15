# #-*- coding: utf-8 -*
#
# class Queue(object):
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def enqueue(self, item):
#         self.items.insert(0,item)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
# class Vertex(object): #创建图的顶点信息以及顶点连接边的信息
#
#     def __init__(self, key):
#         self.id = key
#         self.connectedTo = {}
#
#     def addNeighbor(self, nbr, weight=0): #nbr目标顶点对象的key
#         self.connectedTo[nbr] = weight
#
#     def __str__(self):
#         return str(self.id) + "connectTo" \
#                + str([x.id] for x in self.connectedTo)
#
#     def getConnections(self):
#         return self.connectedTo.keys()
#
#     def getId(self):
#         return self.id
#
#     def getWeight(self, nbr):
#         return self.connectedTo[nbr]
#
# class  Graph(object): #包含所有顶点的主表
#
#     def __init__(self):
#         self.verList = {}
#         self.numVertices = 0
#
#     #将顶点vert加入图中
#     def addVertex(self, key):
#         newVertex = Vertex(key)
#         self.verList[key] = newVertex
#         self.numVertices = self.numVertices + 1
#
#         return newVertex
#
#     def getVertex(self, n):
#         if n in self.verList:
#             return self.verList[n]
#         else:
#             return None
#
#     def __contains__(self, n):
#         return n in self.verList
#
#     #添加有向边， f:fromVert, t:toVert, w:weight/cost 添加带权的有向边
#     def addEdge(self, f, t, cost=0):
#
#         #不存在的顶点先添加
#         if f not in self.verList:
#             nv = self.addVertex(f)
#
#         if t not in self.verList:
#             nv = self.addVertex(t)
#
#         #调用起始顶点的方法添加邻接边
#         self.verList[f].addNeighbor(self.verList[t], cost)
#
#     #返回图中所有顶点列表
#     def getVertices(self):
#         return self.verList.keys()
#
#     def __iter__(self):
#         return iter(self.verList.values())
#
# def buildGraph(wordFile):
#     d = {}
#     g = Graph()
#     wfile = open(wordFile, 'r')
#
#     #创建单词桶，每个桶只有一个字母不同
#     for line in wfile:
#         word = line[:-1]
#
#         for i in range(len(word)):
#             bucket = word[:i] + '_' + word[i+1:]
#
#             if bucket in d:
#                 d[bucket].append(word)
#             else:
#                 d[bucket] = [word]
#
#     #对同一个桶中的单词添加顶点和边界构成图
#     for bucket in d.keys():
#         for word1 in d[bucket]:
#             for word2 in d[bucket]:
#                 if word1 != word2:
#                     g.addEdge(word1, word2)
#
#     return g
#
# def bfs(g, start): #广度遍历
#     '''
#     时间复杂度 v:顶点数量 E:边
#     O(V+E)
#     '''
#     start.setDistance(0)
#     start.setPre(None)
#
#     vertQueue = Queue()
#     vertQueue.enqueue(start)
#
#     while vertQueue.size() > 0:
#         currentVert = vertQueue.dequeue()
#         for nbr in currentVert.getConnections():
#             if nbr.getColor() == "white":
#                 nbr.setColor("gray")
#                 nbr.setDistance(currentVert.getDistance() + 1)
#                 nbr.setPred(currentVert)
#                 vertQueue.enqueue(nbr)
#
#         currentVert.setColor("black")
#
#
# if __name__ == '__main__':
#
#     # g = Graph()
#     # for i in range(6):
#     #     g.addVertex(i)
#     #
#     # g.addEdge(0,1,5)
#     # g.addEdge(0,5,2)
#     # g.addEdge(1,2,4)
#     # g.addEdge(2,3,9)
#     # g.addEdge(3,4,7)
#     # g.addEdge(3,5,3)
#     # g.addEdge(4,0,1)
#     # g.addEdge(5,4,8)
#     # g.addEdge(5,2,1)
#     #
#     # for v in g:
#     #     for w in v.getConnections():
#     #         print("(%s, %s)" % (v.getId(), w.getId()))
#
#     root = "‪E:/BaiDunYunDownload/PythonDSExamplePrograms/PythonDSExamplePrograms/Chapter7/fourletterwords.txt"
#     print(buildGraph(root))
#
#
#
class A(object):
    def __init__(self, a):
        self.a = a
        print(self.a)

    def make_A(self):
        print(f"a等于{self.a}")

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)


    def make_B(self):
        print(f"b等于{self.a}")

C = A(1)
print("------")
D = B(2, 3)



