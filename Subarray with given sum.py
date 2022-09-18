class Solution:
    def subarraySum(self, nums, k) -> int:
        count = 0
        sums = 0
        d = {0: 1}
        for i in nums:
            sums += i
            if sums - k in d:
                count += d[sums - k]
            if sums not in d:
                d[sums] = 1
            else:
                d[sums] += 1
        return count

# driver code
nums=[1,1,1]
k=2
sol=Solution()
print(sol.subarraySum(nums,k))