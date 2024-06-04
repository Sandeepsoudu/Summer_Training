#===calculating length of string==========
# v=input()
# count=0
# for i in v:
#     count+=1
# print(count)
#=======remove  consecutive characters======
# a=input()
# b=[]
# for i in range(len(a)-1):
#     if a[i]!=a[i+1]:
#         b.append(a[i])
# b.append(a[-1])
# print("".join(b))
#===word count===
# s=input().split()
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
#=======remove spaces=====
# v=input()
# spaces=""
# res=""
# for i in v:
#     if i==" ":
#         spaces+=i
#     else:
#         res+=i
# print(spaces+res)
#=====uncommon elements from 2 strings========
# v=input()
# b=input()
# h=[]
# g=[]
# for i in range(len(v)):
#     if v[i] not in b:
#         h.append(v[i])
# for i in range(len(b)):
#     if b[i] not in v:
#         g.append(b[i])
# k="".join(h)
# u="".join(g)
# print(k+u)
#=======uncommon elements from 2 strings=========
# v=input()
# b=input()
# k=v+b
# for i in k:
#     if k.count(i)==1:
#         print(i,end="")
#========maximum occuring character in given string===========
# v=input().lower()
# b=[]
# for i in v:
#     if v.count(i)>1:
#         b.append(i)
# print("".join(set(b)))
#==PRIME NUMBER=-============
# v=int(input())
# count=1
# for i in range(1,v+1):
#     if v%i==0:
#         count+=1
# if count<3:
#     print("prime number")
# else:
#     print("not prime number")


    