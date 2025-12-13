n=1
m=1

for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print("",n,end="")
        n+=1
    n=1
    n=m+1
    m+=m
    print("")