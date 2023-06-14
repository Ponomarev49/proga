import math
ind=[]
for n in range(1,25):
    if n<10:
        f2=open('output_s1_0'+str(n)+'.txt')
        f1= open('input_s1_0'+str(n)+'.txt')
    else:
        f2=open('output_s1_'+str(n)+'.txt')
        f1= open('input_s1_'+str(n)+'.txt')
    put=[]
    k=f1.readline().split()
    otv=0
    n=int(k[0])
    m=int(k[1])
    p=[[math.inf for x in range(0,n+1)] for y in range (0,n+1)]
    q=[0 for x in range(n+1)]
    z=1
    for i in range(0,n): 
        t=f1.readline().split()
        p[int(t[0])][z]=int(t[1])
        p[z][int(t[0])]=int(t[1])
        p[i][i]=0
        p[i+1][i+1]=0
        z+=1
    for i in range(0,m):
         t=f1.readline().split()
         q[int(t[0])]=int(t[1])
    t=f1.readline().split()
    start=int(t[0])
    Z=int(t[1])
    for i in range(n+1):
        if q[i]<Z:
            q[i]=0
    D=p
    Dd=[[0 for x in range (0,n+1)] for y in range(0,n+1)]
    for c in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                Dd[i][j]=min(D[i][c]+D[c][j],D[i][j])
        D=Dd
    for i in range(n+1):
        t=f1.readline().split()
    for i in range(len(q)):
        if q[i]!=0:
            ind.append(i)
    while ind!=[0]*len(ind):
        for i in ind:
            if i!=0:
                put.append(D[start][i])
            else:
                put.append(math.inf) 
        otv+=min(put)
        start=ind[put.index(min(put))]
        ind[put.index(min(put))]=0
        put=[]
    print(str(otv)==f2.read())
