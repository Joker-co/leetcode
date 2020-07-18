class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N==0:
            return 0
        M = len(matrix[0])
        if M==0:
            return 0

        lmax = 0
        dp = [[0]*M for _ in range(N)]
        for i in range(N):
            dp[i][0] = int(matrix[i][0])
            if lmax==0 and dp[i][0]:
                lmax = 1
        for i in range(M):
            dp[0][i] = int(matrix[0][i])
            if lmax==0 and dp[0][i]:
                lmax = 1
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][j]=='0':
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                lmax = max(lmax, dp[i][j])
        return lmax * lmax
