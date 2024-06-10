#========Double linkedlist=================
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, data):
#         if not self.head:
#             self.head = Node(data)
#             self.tail = self.head
#         else:
#             new_node = Node(data)
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node

#     def prepend(self, data):
#         if not self.head:
#             self.head = Node(data)
#             self.tail = self.head
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     def display(self):
#         elements = []
#         cur_node = self.head
#         while cur_node:
#             elements.append(cur_node.data)
#             cur_node = cur_node.next
#         print(elements)

#     def delete(self, data):
#         cur_node = self.head
#         while cur_node:
#             if cur_node.data == data:
#                 if cur_node.prev:
#                     cur_node.prev.next = cur_node.next
#                 else:
#                     self.head = cur_node.next
#                 if cur_node.next:
#                     cur_node.next.prev = cur_node.prev
#                 else:
#                     self.tail = cur_node.prev
#                 return
#             cur_node = cur_node.next

#     def insert_after(self, data, new_data):
#         cur_node = self.head
#         while cur_node:
#             if cur_node.data == data:
#                 new_node = Node(new_data)
#                 new_node.prev = cur_node
#                 new_node.next = cur_node.next
#                 cur_node.next = new_node
#                 if new_node.next:
#                     new_node.next.prev = new_node
#                 else:
#                     self.tail = new_node
#                 return
#             cur_node = cur_node.next

#     def insert_before(self, data, new_data):
#         cur_node = self.head
#         while cur_node:
#             if cur_node.data == data:
#                 new_node = Node(new_data)
#                 new_node.next = cur_node
#                 new_node.prev = cur_node.prev
#                 cur_node.prev = new_node
#                 if new_node.prev:
#                     new_node.prev.next = new_node
#                 else:
#                     self.head = new_node
#                 return
#             cur_node = cur_node.next

# dll = DoublyLinkedList()
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.prepend(0)
# dll.display()  # [0, 1, 2, 3]
# dll.delete(2)
# dll.display()  # [0, 1, 3]
# dll.insert_after(1, 4)
# dll.display()  # [0, 1, 4, 3]
# dll.insert_before(3, 5)
# dll.display()  # [0, 1, 4, 5, 3]
#===========single linked list============
# Create a Node class to create a node
# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.next = None

# # Create a LinkedList class


# class LinkedList:
#     def _init_(self):
#         self.head = None

#     # Method to add a node at begin of LL
#     def insertAtBegin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     # Method to add a node at any index
#     # Indexing starts from 0.
#     def insertAtIndex(self, data, index):
#         new_node = Node(data)
#         current_node = self.head
#         position = 0
#         if position == index:
#             self.insertAtBegin(data)
#         else:
#             while (current_node != None and position + 1 != index):
#                 position = position + 1
#                 current_node = current_node.next

#             if current_node != None:
#                 new_node.next = current_node.next
#                 current_node.next = new_node
#             else:
#                 print("Index not present")

#     # Method to add a node at the end of LL

#     def insertAtEnd(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return

#         current_node = self.head
#         while (current_node.next):
#             current_node = current_node.next

#         current_node.next = new_node

#     # Update node of a linked list
#     # at given position
#     def updateNode(self, val, index):
#         current_node = self.head
#         position = 0
#         if position == index:
#             current_node.data = val
#         else:
#             while (current_node != None and position != index):
#                 position = position + 1
#                 current_node = current_node.next

#             if current_node != None:
#                 current_node.data = val
#             else:
#                 print("Index not present")

#     # Method to remove first node of linked list

#     def remove_first_node(self):
#         if (self.head == None):
#             return

#         self.head = self.head.next

#     # Method to remove last node of linked list
#     def remove_last_node(self):

#         if self.head is None:
#             return

#         current_node = self.head
#         while (current_node.next.next):
#             current_node = current_node.next

#         current_node.next = None

#     # Method to remove at given index
#     def remove_at_index(self, index):
#         if self.head == None:
#             return

#         current_node = self.head
#         position = 0
#         if position == index:
#             self.remove_first_node()
#         else:
#             while (current_node != None and position + 1 != index):
#                 position = position + 1
#                 current_node = current_node.next

#             if current_node != None:
#                 current_node.next = current_node.next.next
#             else:
#                 print("Index not present")

#     # Method to remove a node from linked list
#     def remove_node(self, data):
#         current_node = self.head

#         if current_node.data == data:
#             self.remove_first_node()
#             return

#         while (current_node != None and current_node.next.data != data):
#             current_node = current_node.next

#         if current_node == None:
#             return
#         else:
#             current_node.next = current_node.next.next

#     # Print the size of linked list
#     def sizeOfLL(self):
#         size = 0
#         if (self.head):
#             current_node = self.head
#             while (current_node):
#                 size = size + 1
#                 current_node = current_node.next
#             return size
#         else:
#             return 0

#     # print method for the linked list
#     def printLL(self):
#         current_node = self.head
#         while (current_node):
#             print(current_node.data)
#             current_node = current_node.next


# # create a new linked list
# llist = LinkedList()

# # add nodes to the linked list
# llist.insertAtEnd('a')
# llist.insertAtEnd('b')
# llist.insertAtBegin('c')
# llist.insertAtEnd('d')
# llist.insertAtIndex('g', 2)

# # print the linked list
# print("Node Data")
# llist.printLL()

# # remove a nodes from the linked list
# print("\nRemove First Node")
# llist.remove_first_node()
# print("Remove Last Node")
# llist.remove_last_node()
# print("Remove Node at Index 1")
# llist.remove_at_index(1)

# # print the linked list again
# print("\nLinked list after removing a node:")
# llist.printLL()

# print("\nUpdate node Value")
# llist.updateNode('z', 0)
# llist.printLL()

# print("\nSize of linked list :", end=" ")
# print(llist.sizeOfLL())