# @before-stub-for-debug-begin
from python3problem221 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
import numpy as np
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix: 
            return 0

        h = len(matrix)
        w = len(matrix[0])
        f = np.zeros([h,w])
        max_val = 0

#        for i in range(h):
#            f[i][0] = int(matrix[i][0])
#        for i in range(w):
#            f[0][i] = int(matrix[0][i])


        for i in range(0,h):
            for j in range(0,w):
                if i==0 or j==0:
                    f[i][j] = int(matrix[i][j])
                elif int(matrix[i][j])==1:
                    f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
                max_val = max(max_val,int(f[i][j]))
                
                
        #return int(max(map(max, f)) ** 2)
        return max_val*max_val
                
        
# @lc code=end

