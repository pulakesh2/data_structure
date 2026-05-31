class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

nodep = Node(4)
nodeq = Node(5)

nodep.next = nodeq

nodex = Node(6)

arr = [node1, nodep, nodex]

import heapq

def merge(arr):
    min_heap = []

    for i in range(len(arr)):
        heapq.heappush(min_heap, arr[i])

    while min_heap:
        node_small = heapq.heappop(min_heap)
        node_large = heapq.heappop(arr)

        node = merge_two_node(node_small, node_large)

        heapq.heappush(min_heap, node)

    return min_heap[0]

def merge_two_node(node1, node2):
    temp = node1

    while temp.next is not None:
        temp = temp.next

    temp.next = node2

    return node1

def print_linked_list(node):
    temp = node
    while temp:
        print(temp.data)
        temp = temp.next

head = merge(arr)
print_linked_list(head)
