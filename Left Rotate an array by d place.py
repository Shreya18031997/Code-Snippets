class Solution:
    def reverse(self, nums, i, j):
        while (i <= j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # reverse n-k array
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        return nums

li=[-1,-100,3,99]
k=2
sol=Solution()
print(sol.rotate(li,k))
