def largest(arr, n):
    for i in range(1,n):
        if arr[0]<arr[i]:
            arr[0]=arr[i]
    return arr[0]


# main
n=int(input())
arr=[]
for i in range(n):
    value=int(input())
    arr.append(value)
print(largest(arr, n))