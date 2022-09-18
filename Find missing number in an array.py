class Solution:
    def missingNumber(self, nums) -> int:
        sum = 0
        for i in range(len(nums) + 1):
            sum += i
        for i in nums:
            sum -= i
        return sum

# driver sum
nums=[3,0,1]
sol=Solution()
print(sol.missingNumber(nums))