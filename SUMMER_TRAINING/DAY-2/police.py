n=int(input("enter cases:"))
crimes=0
pol=0
for i in range(n):
    e=int(input())
    if e==-1:
        if crimes>0:
            crimes-=1
        else:
            pol+=1
    else:
        crimes+=1
print(pol)
    
