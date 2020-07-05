'''
使用动态规划
因为有负数的存在
较小值乘以负数为较大值，较大值乘以负数为较小值
状态：dp[i]为以第i个数字结尾的连续子串的乘积
状态转移：需要同时记录某一索引元素结尾的子串最大值与最小值
'''

class Solution:
    def maxProduct(self, nums) -> int:
        leng = len(nums)
        num_max = nums[0]
        
        dp_min = [0]*leng
        dp_max = [0]*leng
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        
        for i in range(1,leng):
            if nums[i]>=0:
                dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])
                dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
            else:
                dp_min[i] = min(dp_max[i-1]*nums[i], nums[i])
                dp_max[i] = max(dp_min[i-1]*nums[i], nums[i])
        
        for i in range(1, leng):
            num_max = max(num_max, dp_max[i])
        
        return num_max
