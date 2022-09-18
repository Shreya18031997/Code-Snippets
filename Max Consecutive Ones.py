class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        c = 0
        count = 0
        for i in nums:
            if i != 1:
                if c > count:
                    count = c
                c = 0
            else:
                c += 1
        if c > count:
            count = c
        return count

nums=[1,1,0,1,1,1]
sol=Solution()
print(sol.findMaxConsecutiveOnes(nums))
