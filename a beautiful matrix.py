aee=[]
for i in range(5):
        arr =list([int(x) for x in input().split()])
        aee.append(arr)
for j in range(5):
        if int(aee[j][i])==1:
                print(abs(int(j+1) - 3)+abs(int(i+1) - 3))
                break






