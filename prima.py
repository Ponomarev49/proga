u=['ab','ac','ae','bc','bd','be','ce','de','df','dg','dh','eg','fh','gh']
v=[2   ,2   ,7   ,2   ,9   ,2   ,5   ,10  ,5   ,2   ,16  ,9   ,17  ,  17]
otv=[]
l=0
f='false'
mn=0
r=0
n=8
print("выберите одну из вершин")
otv.append((input()))
while len(otv)<n:
    for i in range(0,len(otv)):
        for j in range(len(u)):
            if otv[i] in u[j]:
                if f=='false':
                    f='true'
                    mn=v[j]
                    r=j
                else:
                    if mn>v[j]:
                        mn=v[j]
                        r=j
    if (u[r][0] in otv and u[r][1] in otv):
        u.pop(r)
        v.pop(r)
    elif (u[r][0] in otv and u[r][1]  not in otv):
        otv.append(u[r][1])
        l+=mn
        u.pop(r)
        v.pop(r)
    else :
        otv.append(u[r][0])
        l+=mn
        u.pop(r)
        v.pop(r)
    f='false'
    mn=0
print(l)
