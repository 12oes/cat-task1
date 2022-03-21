n=int(input())
x=int(input())
y=int(input())
z=int(input())
list2=[]
list3=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k !=n:
                list2=[i,j,k]
                list3.append(list2)
print(list3)







