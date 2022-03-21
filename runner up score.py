n = int(input())
arr = [int(x) for x in input().split()]
m = max(arr)
for i in range(len(arr)-1,0,-1):
    if arr[i]==m:
        arr.remove(arr[i])
k=max(arr)
print(k)




