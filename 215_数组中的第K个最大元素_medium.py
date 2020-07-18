class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        beg, end = 0, len(nums)-1
        idx = -1

        while idx != k-1:
            beg_b = beg
            end_b = end
            tmp = nums[beg]
            while beg<end:
                while beg<end and nums[end]<tmp:
                    end -= 1
                if beg<end:
                    nums[beg] = nums[end]
                    beg += 1
                while beg<end and nums[beg]>tmp:
                    beg += 1
                if beg<end:
                    nums[end] = nums[beg]
                    end -= 1
            nums[beg] = tmp
            idx = beg
            if idx>k-1:
                beg = beg_b
                end = idx-1
            if idx<k-1:
                beg = idx+1
                end = end_b
        return nums[idx]
