def missingNumber(A, N):
    # Your code goes here
    sums = 0
    for i in range(N + 1):
        sums += i
    for i in A:
        sums -= i
    return sums

# driver code
n=4
a=[1,4,3]
print(missingNumber(a,n))
