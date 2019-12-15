import math


achieve = False
achieve2= False

class Node(object):
    def __init__(self, size,depth):
        self.ID = ""
        self.status = 0         #初始空闲
        self.size   = size      #初始大小
        self.left   = None      #左节点
        self.right  = None      #右节点
        self.depth  = depth     #创建深度

class Operation(object):
    def __init__(self,maxlen,minlen):
        self.maxlen = int(math.pow(2,maxlen))   #math.pow   计算x的y次方
        self.minlen = int(math.pow(2,minlen))
        self.result = []
        self.root   = Node(self.maxlen, 0)      #初始化节点

    def allocate(self,size,ID):
        global achieve
        global achieve2
        level = 0   #裂变的层数

        for i in range(10):
            #查询适合的储存页大小
            if size <= self.maxlen//math.pow(2,i) and size > self.maxlen//math.pow(2,i+1):
                level = i
            break
        print("搜索深度为",level)
        print("将要分配的节点是：",ID)

        if self.root.left is None and self.root.right is None:
            p = self.root
            for i in range(level):
                p.status = 1
                p.left = Node(p.size/2,i+1)
                p.right= Node(p.size/2,i+1)
                p      =p.left
            p.status   = 1  







        super().__init__(*args, **kwargs)