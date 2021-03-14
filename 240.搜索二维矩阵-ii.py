# @before-stub-for-debug-begin
from python3problem240 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        rows = len(matrix)
        cols = len(matrix[0])
        i=0
        j = cols-1
        while i < rows and j>=0:
                if matrix[i][j] > target:
                    j -= 1
                elif matrix[i][j] < target:
                    i += 1
                else:
                    return True
        
        return False
        


        
# @lc code=end

