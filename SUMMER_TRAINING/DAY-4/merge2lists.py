# li1=list(map(int,input().split()))
# li2=list(map(int,input().split()))
# merge=sorted(li1+li2)
# print(merge)
#======list and sort based on its length=====
# a=input().split()
# a.sort(key=len)
# print(a[::-1])
#=====swap first and last ele in list=======
# a=input().split()
# a[-1],a[0]=a[0],a[-1]
# print(a)
#======remove duplicates from list==========
# a=input().split()
# b=list(set(a))
# print(b)
#====2nd logic======
# a=input().split()
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
#======print odd number of times========
# a=input().split()
# c=[]
# for i in a:
#     if a.count(i)%2!=0 and i not in c:
#         c.append(i)
# print(c)
#======sum of minimum 3 elements in list after removing duplicates===
#a=list(map(int,input().split()))
# a.sort()
# b=list(set(a))
# print(sum(b[:3]))
#======even elements first in descending and odd ele in descending==========
# a=list(map(int,input().split()))
# b=[]
# c=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
#     else:
#         c.append(i)
# v=b[::-1]
# c.sort()
# print(v+c)
# Read the list of integers
# a = list(map(int, input().split()))
# b,c=map(int,input().split())
# d = []
# for i in a:
#     if i in range(b,c+1):
#         d.append(i)  
# print(d)
# mul = 1
# for i in range(len(d)):
#     mul *= d[i]
# print(mul)
# n=int(input())
# #list in list
# li=[map(int,input().split()) for i in range(n)]
# sum1=0
# for i in li:
#     s=sum(i)
#     if  s>sum1:
#         sum1=s
#         inde=li.index(i)
# print(inde)
#===========remove tuples======
a=input().split()
b=[]
for i in a:
    if i!='()':
        b.append(i)
print(b)


