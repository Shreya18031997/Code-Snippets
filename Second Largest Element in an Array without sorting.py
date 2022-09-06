def print2largest(arr, n):
    # code here
    # finding minimum and maximum element
    for i in range(1, n):
        if arr[0] < arr[i]:
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
        if arr[1] > arr[i]:
            temp = arr[1]
            arr[1] = arr[i]
            arr[i] = temp
    # replacing max element with minimum element
    for i in range(1, n):
        if arr[i] == arr[0]:
            arr[i] = arr[1]
    # comparing element for largest now
    for i in range(1, n):
        if arr[i] > arr[1]:
            arr[1] = arr[i]

    if n < 2 or arr[0] == arr[1]:
        return -1
    return arr[1]


# main
n=int(input())
arr=[]
for i in range(n):
    value=int(input())
    arr.append(value)
print(print2largest(arr, n))