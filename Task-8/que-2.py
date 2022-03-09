import numpy as n
ary1=n.array([10,12,13,14,15])
ary2=n.array([10,12,13,14,15])
a=True
for i in range(0,ary1.__len__()):
    if ary1[i]==ary2[i]:
        a=True
    else:
        a=False
        break
print(a)    
