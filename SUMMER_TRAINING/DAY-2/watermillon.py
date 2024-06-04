def watermillon():
    weight=int(input("enter the weight:"))
    if weight%2!=0:
        return False
    mid=weight//2
    if mid%2==0:
        return True
    else:
        return False
print(watermillon())