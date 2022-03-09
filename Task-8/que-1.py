import numpy as n
ary=[]
nz=5
first=int(input("Enter first number:"))
last=int(input("Enter last number:"))
for i in range(first,last+1):
    ary.append(i)
z=n.array(ary)
k=n.zeros(len(z) + (len(z)-1)*(nz))
k[::nz+1]=z
print(k)