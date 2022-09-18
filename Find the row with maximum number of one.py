class Solution:
    def rowWithMax1s(self, arr, n, m):
        max_count = 0
        indexi = -1
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    count = m - j
                    if count > max_count:
                        max_count = count
                        indexi = i
                        break
        return indexi

# driver code
arr=[[0,0],[1,1]]
n=2
m=2
sol=Solution()
print(sol.rowWithMax1s(arr,n,m))