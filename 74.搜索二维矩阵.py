# @before-stub-for-debug-begin
from python3problem74 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        col = len(matrix[0])
        row = len(matrix)
        st,ed = 0,row*col-1

        # mid = i*col+j
        while(st<=ed):
            mid = st + int((ed-st)/2)
            i = mid // col 
            j = mid % col 
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: ed = mid - 1
            else: st = mid + 1
        
        return False
# @lc code=end

