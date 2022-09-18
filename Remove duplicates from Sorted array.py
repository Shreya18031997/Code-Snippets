class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1

li=[0,0,1,1,1,2,2,3,3,4]
sol=Solution()
print(sol.removeDuplicates(li))