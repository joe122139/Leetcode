# @before-stub-for-debug-begin
#from python3problem37 import *
#from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

from typing import List
# @lc code=start
class Solution:
    def __init__(self):
        self.flag = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        h_r=[set() for i in range(9)]
        h_c=[set() for i in range(9)]
        h_sq=[[set() for i in range(3)] for i in range(3)]
        row  = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                nums = board[i][j]
                if nums == '.': continue
                h_c[j].add(nums)
                h_r[i].add(nums)
                h_sq[i//3][j//3].add(nums)
        
        def backTracking(i,j):
            if board[i][j]!='.':
                if i==8 and j==8:
                    self.flag = True
                    return
                if j<8:
                    backTracking(i,j+1)
                else:
                    backTracking(i+1,0)
                return

            for cand in range(1,10):
                cand = str(cand)
                if cand not in h_r[i] and cand not in h_c[j] and cand not in h_sq[i//3][j//3]:
                    board[i][j] = cand
                    h_r[i].add(cand)
                    h_c[j].add(cand)
                    h_sq[i//3][j//3].add(cand)
                    if i==8 and j==8:
                        self.flag = True
                        return 
                    if j<8:
                        backTracking(i,j+1)
                    elif i<8:
                        backTracking(i+1,0)
                    if self.flag: return
                    board[i][j] = '.'
                    h_r[i].remove(cand)
                    h_c[j].remove(cand)
                    h_sq[i//3][j//3].remove(cand)

        self.flag = False
        backTracking(0,0)
        print(board)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ary = [1,2]
    ary = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(ary)


