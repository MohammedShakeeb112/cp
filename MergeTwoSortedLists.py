class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next = n
        self.prev = p

    # def printNode(self):
    #     return self.data

    # def __str__(self):
    #     return str(self.data)

# n = Node(25)
# print(n, type(n), n.data, type(n.data), n.printNode(), type(n.printNode()))

# N = Node([61, 12, 41])
# print(N, type(N), N.data, type(N.data), N.printNode(), type(N.printNode()), N.data[2], type(N.data[2]), N.printNode()[2], type(N.printNode()[2]))

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        cur_node = self.root
        while cur_node:
            if cur_node.data == d:
                return True
            else:
                cur_node = cur_node.next
        return False

    def remove(self, d):
        cur_node = self.root
        prev_node = None
        while cur_node:
            if cur_node.data == d:
                if prev_node:
                    prev_node.next = cur_node.next
                else:
                    self.root = cur_node.next
                self.size -= 1
                return True
            else:
                prev_node = cur_node
                cur_node = cur_node.next
        return False

    def printlist(self):
        cur_node = self.root
        while cur_node:
            print(cur_node.data, end='->')
            cur_node = cur_node.next
        print('NONE')

l1 = LinkedList()
l1.add(6)
l1.add(2)
l1.add(1)

l2 = LinkedList()
l2.add(4)
l2.add(3)
l2.add(1)

# l1.printlist()
# l2.printlist()

#return list
# def addtwolist(l1, l2):
#     result = []
#     while l1.root and l2.root:
#         # print(l1.root)
#         if l1.root.data <= l2.root.data:
#             v1 = l1.root.data
#             v2 = l2.root.data
#             # print(val)
#             result.append(v1)
#             result.append(v2)
#             l1.root = l1.root.next
#             l2.root = l2.root.next
#         else:
#             l1.root.data, l2.root.data = l2.root.data, l1.root.data 
#     return result   

#return listnode
def addtwolist(l1, l2):
    if l1 and l2:
        if l1.root > l2.root:
            pass
    

# print(addtwolist(l1, l2))