class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<1 or k<1 or k>len(nums):
            return []
        
        dmax = []
        beg, end = 0, 0
        while end-beg+1<=k:
            if len(dmax):
                while len(dmax)>0 and nums[end]>dmax[-1]:
                    dmax.pop()
            dmax.append(nums[end])
            end += 1
        
        res = [dmax[0]]
        while end<len(nums):
            if nums[beg]==dmax[0]:
                del(dmax[0])
            beg += 1
            
            while len(dmax)>0 and nums[end]>dmax[-1]:
                dmax.pop()
            dmax.append(nums[end])
            res.append(dmax[0])
            end += 1
        return res
