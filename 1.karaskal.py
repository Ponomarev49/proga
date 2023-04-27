k=9
U=[12,15,14,23,24,25,35,36,45,47,48,56,58,59,78,89]
V=[15,14,23,19,16,15,14,26,25,23,20,24,27,18,14,18]
otv=[[]]
f1="false"
f2="false"
x1=0
x2=0
l=0
otv[0].append(U[V.index(min(V))]%10)
otv[0].append(U[V.index(min(V))]//10)
k1=2
l+=min(V)
U.pop(V.index(min(V)))
V.pop(V.index(min(V)))
while k1<k:
    mn=min(V)
    i=V.index(min(V))
    for j in range(0,len(otv)):
        if U[i]%10 in otv[j]:
            f1="true"
            x1=j
        if U[i]//10 in otv[j]:
            f2="true"
            x2=j
    if (f1=="false")and(f2=="false"):
        otv.append([])
        otv[len(otv)-1].append(U[i]%10)
        otv[len(otv)-1].append(U[i]//10)
        U.pop(i)
        V.pop(i)
        l+=mn
        k1+=2
    if (f1=="true")and(f2=="true")and(x1==x2):
        U.pop(i)
        V.pop(i)
    if (f1=="true")and(f2=="true")and(x1!=x2):
        otv[x1]+=otv[x2]
        otv.pop(x2)
        l+=mn
        U.pop(i)
        V.pop(i)
    if (f1=="true")and(f2=="false"):
        otv[x1].append(U[i]//10)
        l+=mn
        k1+=1
        U.pop(i)
        V.pop(i)
    if (f1=="false")and(f2=="true"):
        otv[x2].append(U[i]%10)
        l+=mn
        k1+=1
        U.pop(i)
        V.pop(i)
    f1="false"
    f2="false"
print(l)
