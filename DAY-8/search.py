#======LINEAR SEARCH========
# def linear(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return "element found at index",i
#     return "not found"
# arr=list(map(int,input().split()))
# target=int(input())
# print(linear(arr,target))

#=======binary search========
# def binary(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<right:
#         mid=left+right//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# arr=list(map(int,input().split()))
# target=int(input())
# v=binary(arr,target)
# if v!=-1:
#     print("element is found")
# else:
#     print("not found")
a=['h','i']
for i in a[::-1]:
    print(i,end=" ")