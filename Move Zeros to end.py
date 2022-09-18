class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[c]
                nums[c]=temp
                c+=1

li=[0,1,0,3,12]
sol=Solution()
sol.moveZeroes(li)
print(li)