class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return nums
        
        right = [0]*(len(nums)+1)
        right[-1] = 1
        for i in range(len(nums)-1, -1, -1):
            right[i] = nums[i]*right[i+1]
        
        left = 1
        res = [0]*len(nums)
        for i in range(len(res)):
            res[i] = left*right[i+1]
            left *= nums[i]
        return res
