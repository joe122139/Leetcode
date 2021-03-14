# @before-stub-for-debug-begin
from python3problem62 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
import numpy as np
class Solution:
    '''
    2D
    def uniquePaths(self, m: int, n: int) -> int:
        
        a = np.zeros([m,n])
        a[0][0]=1
        for i in range(1,m):
            a[i][0] = 1
        for i in range(1,n):
            a[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                a[i][j] = a[i-1][j] + a[i][j-1]
        
        return int(a[m-1][n-1])
    '''
    #1D
    def uniquePaths(self, m: int, n: int) -> int:
        
        a = np.zeros(n)
        a[0]=1
        for i in range(1,n):
            a[i] = 1

        for i in range(1,m):
            for j in range(1,n):
                a[j] = a[j-1] + a[j]
        
        return int(a[n-1])
# @lc code=end

