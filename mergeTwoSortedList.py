# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
# https://leetcode.com/problems/merge-two-sorted-lists/
 

# Example 1:

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: l1 = [], l2 = []
# Output: []

# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]

 

# Constraints:

#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both l1 and l2 are sorted in non-decreasing order.

# def mergeTwoSort(self, a,b):
#     if a and b:
#         if a.val > b.val:
#             a, b = b, a
#         a.next = self.mergeTwoSort(a.next, b)
#     return a or b


class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def printNode(self):
        return self.data
    
    def __str__(self):
        return str(self.data)

# n = Node(25)
# print(n , type(n), n.printNode(), type(n.printNode()))
# n = Node([12,8,35])
# print(n, type(n), n.printNode(), type(n.printNode()), n.printNode()[2], type(n.printNode()[2]))

class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        this_node = Node(d, self.root)
        self.root = this_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_Node = None
        while this_node is not None:
            if this_node.data == d:
                if prev_Node is not None:
                    prev_Node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_Node = this_node
                this_node = this_node.next_node
        return False

    def printLinkedList(self):
        this_node = self.root
        while this_node is not None:
            print(this_node.data, end='->')
            this_node = this_node.next_node
        print('NONE')

l1 = LinkedList()
l1.add(4)
l1.add(2)
l1.add(1)

l2 = LinkedList()
l2.add(4)
l2.add(3)
l2.add(1)

# l1.printLinkedList()
# l2.printLinkedList()

def mergeTwolist(a,b):
    # print(a.root)
    # a = a.root
    # b = b.root
    # print(l1.next_node.next_node.next_node)
    # root = n = Node(0)
    # v1 = v2 = 0
    # while l1 or l2 is not None:
    #     if l1:
    #         v1 = l1.data
    #         l1 = l1.next_node
    #     if l2:
    #         v2 = l2.data
    #         l2 = l2.next_node


    if a and b:
        # print(a.root.data, b.root.data)
        if a.root.data > b.root.data:
            a.root, b.root = b.root, a.root
            print('if',a.root, b.root)
        a.next_node = mergeTwolist(a.next_node, b.root)
        print(a.data, b.data)
    # return a or b
        

mergeTwolist(l1, l2)