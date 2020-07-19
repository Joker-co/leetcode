# 动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = i
            limit = int(sqrt(i))
            for j in range(1, limit+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
 
 # BFS
 class Solution:
    def numSquares(self, n: int) -> int:
        if n==0:
            return 0
        
        datas = [[n,0]]
        visited = [0]*(n+1)
        visited[n] = 1

        while len(datas):
            tmp = datas.pop(0)
            limit = int(sqrt(tmp[0]))+1
            for i in range(1, limit):
                ntmp = [tmp[0]-i*i, tmp[1]+1]
                if ntmp[0]==0:
                    return ntmp[1]
                if visited[ntmp[0]]==0:
                    datas.append(ntmp[:])
                    visited[ntmp[0]] = 1
        return -1
