list1=[[1,'Chaitanya',90],[2,'Satish',95],[3,'Aditya',85]]
list2=['Rollno','Name','Marks']                          
for f in range(0,len(list2)):                           
    print(list2[f],end='  ')
print()

for g in range(0,len(list1)):                          
    print()
    for f in range(0,len(list1)):
        print(list1[g][f],end='    ')
print()

print(list1[1])
