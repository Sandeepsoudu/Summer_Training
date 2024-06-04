# def dic():    
#     di={1:10,2:20,3:30,4:40,5:50,6:60}
#     v=2
#     for i in di.keys():
#         if v==i:
#             return "key is present in the dictionary"
#     return "key is not present in the dictionary"
# print(dic())
#================
# n=int(input())
# dict=[]
# for i in range(1,n+1):
#     dict.append({i:i*i})
# print(dict)
#===========user input for dictinary=======
# d={}
# n=int(input())
# for i in range(n):
#     key=input()
#     value=input()
#     d[key]=value
# print(d)
#=======merge 2 dictionaries============
# d={1:2,3:4}
# d2={5:6}
# v=d.update(d2)
# print(d)
#===========remove key from dict========
# n=int(input())
# d={}
# for i in range(n):
#     key=input()
#     value=input()
#     d[key]=value
# m=input()
# if m in d:
#     del d[m]
# print(d)
#==========map 2 lists into a dictionary=====
# n=input().split()
# m=input().split()
# d={}
# for i in range(len(n)):
#     key=n[i]
#     value=m[i]
#     d[key]=value
# print(d)
#============combined 2 dictionaries and add common keys===
# n=int(input("enter the elements from dict1:"))
# d={}
# for i in range(n):
#     key=input("enter key:")
#     value=int(input("enter value:"))
#     d[key]=value
# d1={}
# m=int(input("enter the elements from dict2:"))
# for i in range(m):
#     key=input("enter key:")
#     value=int(input("enter value:"))
#     d1[key]=value

# for key in d1:
#     if key in d:
#         d[key]+=d1[key]
#     else:
#         d[key]=d1[key]                   
# print("combined dictionary",d)


