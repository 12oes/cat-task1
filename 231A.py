n = int(input(" "))
list1=[]
c=0
for i in range(n):
    l=[int(x) for x in input().split()]
    list1.append(l)
for i in range(n):
    if sum(list1[0], 0) >= 2:
        c+=1
print(c)




