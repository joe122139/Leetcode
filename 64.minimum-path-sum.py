#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
import numpy as np
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s = np.zeros([m,n])
        s[0][0] = grid[0][0]

        for i in range(1,m):
            s[i][0] = s[i-1][0] + grid[i][0]

        for i in range(1,n):
            s[0][i] += s[0][i-1] + grid[0][i]

        for i in range(1,m):
            for j in range(1,n):
                s[i][j] = min(s[i-1][j], s[i][j-1]) + grid[i][j]
                
        return int(s[m-1][n-1])
        
# @lc code=end

