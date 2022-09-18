class Solution:
    def singleNumber(self, nums) -> int:
        r=0
        for i in nums:
            r^=i
        return r

# driver code
nums=[2,2,1]
sol=Solution()
print(sol.singleNumber(nums))