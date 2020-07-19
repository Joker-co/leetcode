class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg,end = 0,0

        while end<len(nums):
            while beg<len(nums) and nums[beg]!=0:
                beg += 1
            if beg>end:
                end = beg + 1
            else:
                end += 1
            while end<len(nums) and nums[end]==0:
                end += 1
            if beg<len(nums) and end<len(nums):
                nums[beg],nums[end] = nums[end],nums[beg]
        return nums
