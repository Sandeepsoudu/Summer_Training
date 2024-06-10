# class Stack:
#     def _init_(self):
#         self.items = []
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def push(self,item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("pop from an empty stack")
        
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("peek from an empty stack")
        
#     def size(self):
#         return len(self.items)
    

# stack = Stack()
# print("Is the stack empty?", stack.is_empty())
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print("Stack:", stack.items)
# print("Top of the stack:", stack.peek())
# print("pop:", stack.pop())
# print("Stack after pop:", stack.items)
# print("Is the stack empty?", stack.is_empty)
# print("Is the stack empty;", stack.size())
# a=[0,0,1,1,1,1,2,3,3]
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# b=[]
# for i in d:
#     if d[i]==2:fffffffffffffffffffffffffffffffffffffv
#         b.append(i)
#         b.append(i)
#     elif d[i]==1:
#         b.append(i)
#     if d[i]>=3:
#         b.append(i)
#         b.append(i)
# print(b).
#valid parenthesis=======
# def valid():
#     s=input()
#     v=[]
#     for i in s:
#         if i=="(":
#             v.append(")")
#         if i=="[":
#             v.append("]")
#         if i=="{":
#             v.append("}")
#         if not v or v.pop()!=i:
#             return False
#     return not v
# print(valid())
# def check(s,t):
#     b=[]
#     for i in t:
#         if i in s:
#             return 0
#         if i not in s:
#             b.append(i)
#         for i in s:
#             if i not in t:
#                 return len(t)
#     print(b)
#     return len(b)
# s=input()
# t=input()
# print(check(s,t))
#=========Tree Traversal techniques============
class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def iot(node):
    if node is not None:
        iot(node.left)
        print(node.value,end=" ")
        iot(node.right)
obj=Node(2)
obj.left=Node(3)
obj.right=Node(4)
obj.left.left=Node(6)
obj.left.right=Node(7)
iot(obj)

