# @before-stub-for-debug-begin
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h_r=[{} for i in range(9)]
        h_c=[{} for i in range(9)]
        h_sq=[{} for i in range(9)]
        row  = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                nums = board[i][j]
                if nums == ".": continue
                nums = int(nums)
                h_r[i][nums] = h_r[i].get(nums,0) + 1
                h_c[j][nums] = h_c[j].get(nums,0) + 1
                box_idx = i//3*3 + j//3
                h_sq[box_idx][nums] = h_sq[box_idx].get(nums,0) + 1

                if h_r[i][nums]>1 or h_c[j][nums]>1 or h_sq[box_idx][nums]>1:
                    print(i,j,box_idx,nums)
                    return False
                j+=1
            i+=1
        return True


# @lc code=end

