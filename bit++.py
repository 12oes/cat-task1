x=0
statement=[]
list1=[]
n=int(input())
for i in range(n):
    statement=input()
    list1.append(statement)
for i in range(n):
    if list1[i][1]=='+':
        x=x+1
    else:
        x=x-1
print(x)
