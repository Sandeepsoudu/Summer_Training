def check():  
    dist=int(input("enter distance"))
    if dist<=5:
        return 1
    elif(dist%5==0):
        return dist/5
    else:
        return (dist//5)+1
print(check())


