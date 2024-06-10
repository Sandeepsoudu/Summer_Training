# def selection(arr):
#     for i in range(len(arr)):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min]:
#                 min=j
#         arr[i],arr[min]=arr[min],arr[i]
#     return arr
# arr=list(map(int,input().split()))
# print(selection(arr))
#=======insertion sort=============
def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[i]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=list(map(int,input().split()))
print(insertion(arr))