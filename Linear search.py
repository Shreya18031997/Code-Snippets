class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for i in arr:
            if i==K:
                return 1
        return -1


li=[1,2,3,4,6]
n=5
k=6
sol=Solution()
print(sol.searchInSorted(li,n,k))