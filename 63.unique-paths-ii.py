# @before-stub-for-debug-begin
from python3problem63 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
import numpy as np
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0]=1
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0]==1)

        for i in range(1,n):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1]==1)

        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j]==1):
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1])
        
        return int(obstacleGrid[m-1][n-1])

        
# @lc code=end

