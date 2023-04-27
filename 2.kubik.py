f1=[]
f=open('input_s1_19.txt','r')
f1=f.readlines()
for i in range(0,len(f1),1):
    f1[i]=f1[i].split(" ")
n=int(f1[0][0])
m=int(f1[0][1])
x=int(f1[1][0])
y=int(f1[1][1])
z=int(f1[1][2])
f1.pop(0)
f1.pop(0)
for i in range(0,m,1):
    if (f1[i][0]=="Z") and (z==int(f1[i][1])):      ####для Z
        if (x+y<=n+1):
            mn=min(x,y)
            r=n-2*(mn-1)
            mx=mn+(r-1)
        else:
            mx=max(x,y)
            r=n-2*(n-mx)
            mn=mx-(r-1)
        if int(f1[i][2])==-1:   ##### -1           
            if ((y<x)and(x+y-2*(mn-1)<r+1))or((x==mn)and (y==mn)):
                y=mx-(mx-x)
                x=mx
                continue;
            if ((y<x)and(x+y-2*(mn-1)>r+1))or((x==mx)and (y==mn)):
                x=mx-(y-mn)
                y=mx
                continue;
            if ((y>x)and(x+y-2*(mn-1)>r+1))or((x==mx)and (y==mx)):
                y=mx-(mx-x)
                x=mn
                continue;
            if ((y>x)and(x+y-2*(mn-1)<r+1))or((x==mn)and (y==mx)):
                x=mx-(y-mn)
                y=mn
                continue;
        if int(f1[i][2])==1: ##### 1
            if ((y<x)and(x+y-2*(mn-1)<r+1))or((x==mn)and (y==mn)):
                y=mx-(x-mn)
                x=mn
                continue;
            if ((y<x)and(x+y-2*(mn-1)>r+1))or((x==mx)and (y==mn)):
                x=mx-(mx-y)
                y=mn
                continue;
            if ((y>x)and(x+y-2*(mn-1)>r+1))or((x==mx)and (y==mx)):
                y=mx-(x-mn)
                x=mx
                continue;
            if ((y>x)and(x+y-2*(mn-1)<r+1))or((x==mn)and (y==mx)):
                x=mx-(mx-y)
                y=mx
                continue;
    if (f1[i][0]=="Y")and (y==int(f1[i][1])):                                 ####для Y
        if (x+z<=n+1):
            mn=min(x,z)
            r=n-2*(mn-1)
            mx=mn+(r-1)
        else:
            mx=max(x,z)
            r=n-2*(n-mx)
            mn=mx-(r-1)
        if int(f1[i][2])==-1:   ##### -1           
            if ((z<x)and(x+z-2*(mn-1)<r+1))or((x==mn)and (z==mn)):
                z=mx-(mx-x)
                x=mx
                continue;
            if ((z<x)and(x+z-2*(mn-1)>r+1))or((x==mx)and (z==mn)):
                x=mx-(z-mn)
                z=mx
                continue;
            if ((z>x)and(x+z-2*(mn-1)>r+1))or((x==mx)and (z==mx)):
                z=mx-(mx-x)
                x=mn
                continue;
            if ((z>x)and(x+z-2*(mn-1)<r+1))or((x==mn)and (z==mx)):
                x=mx-(z-mn)
                z=mn
                continue;
        if int(f1[i][2])==1: ##### 1
            if ((z<x)and(x+z-2*(mn-1)<r+1))or((x==mn)and (z==mn)):
                z=mx-(x-mn)
                x=mn
                continue;
            if ((z<x)and(x+z>r+1))or((x==mx)and (z==mn)):
                x=mx-(mx-z)
                z=mn
                continue;
            if ((z>x)and(x+z-2*(mn-1)>r+1))or((x==mx)and (z==mx)):
                z=mx-(x-mn)
                x=mx
                continue;
            if ((z>x)and(x+z-2*(mn-1)<r+1))or((x==mn)and (z==mx)):
                x=mx-(mx-z)
                z=mx
                continue;
    if (f1[i][0]=="X")and (x==int(f1[i][1])):                               ####для X
        if (z+y<=n+1):
            mn=min(z,y)
            r=n-2*(mn-1)
            mx=mn+(r-1)
        else:
            mx=max(z,y)
            r=n-2*(n-mx)
            mn=mx-(r-1)
        if int(f1[i][2])==-1:   ##### -1           
            if ((z<y)and(z+y-2*(mn-1)<r+1))or((y==mn)and (z==mn)):
                z=mx-(mx-y)
                y=mx
                continue;
            if ((z<y)and(z+y-2*(mn-1)>r+1))or((y==mx)and (z==mn)):
                y=mx-(z-mn)
                z=mx
                continue;
            if ((z>y)and(z+y-2*(mn-1)>r+1))or((y==mx)and (z==mx)):
                z=mx-(mx-y)
                y=mn
                continue;
            if ((z>y)and(z+y-2*(mn-1)<r+1))or((y==mn)and (z==mx)):
                y=mx-(z-mn)
                z=mn
                continue;
        if int(f1[i][2])==1: ##### 1
            if ((z<y)and(z+y-2*(mn-1)<r+1))or((y==mn)and (z==mn)):
                z=mx-(y-mn)
                y=mn
                continue;
            if ((z<y)and(z+y-2*(mn-1)>r+1))or((y==mx)and (z==mn)):
                y=mx-(mx-z)
                z=mn
                continue;
            if ((z>y)and(z+y-2*(mn-1)>r+1))or((y==mx)and (z==mx)):
                z=mx-(y-mn)
                y=mx
                continue;
            if ((z>y)and(z+y-2*(mn-1)<r+1))or((y==mn)and (z==mx)):
                y=mx-(mx-z)
                z=mx
                continue;
print(x,y,z)


