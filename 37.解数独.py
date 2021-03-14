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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h_r=[{} for i in range(9)]
        h_c=[{} for i in range(9)]
        h_sq=[{} for i in range(9)]
        row  = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                nums = board[i][j]
                if nums == "." or nums==-1: continue
                nums = int(nums)
                h_r[i][nums] = h_r[i].get(nums,0) + 1
                h_c[j][nums] = h_c[j].get(nums,0) + 1
                box_idx = i//3*3 + j//3
                h_sq[box_idx][nums] = h_sq[box_idx].get(nums,0) + 1

                if h_r[i][nums]>1 or h_c[j][nums]>1 or h_sq[box_idx][nums]>1:
                    print('----',i,j,nums,'hr:',h_r[i][nums],'hc:',h_c[j][nums],'h_sq:',h_sq[box_idx][nums])
                    return False
                j+=1
            i+=1
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row  = len(board)
        col = len(board[0])
        label = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                nums = board[i][j]
                if nums == ".": 
                    label[i][j] = 2
                    continue

        def backTracking(board,i,j,row,col,label):
            if label[i][j]!=2: 
                if j+1<col:
                    backTracking(board,i,j+1,row,col,label)
                elif i+1<row:
                    j = 0
                    backTracking(board,i+1,j,row,col,label)
                else:
                    return
            else:
                #for cand in [1,2,3,4,5,6,7,8,9,-1](1,10):
                for cand in [1,2,3,4,5,6,7,8,9]:
                    board[i][j] = cand
                    print(i,j,cand)
                    if self.isValidSudoku(board):
                        if j+1<col:
                            backTracking(board,i,j+1,row,col,label)
                            board[i][j+1] = -1
                        elif i+1<row:
                            j = 0
                            backTracking(board,i+1,j,row,col,label)
                            board[i+1][j] = -1
#                    elif cand==9:
#                        print('reaching 10')
#                        board[i][j] = -1
#                        return

        backTracking(board,0,0,row,col,label)
        print(board)
        print(label)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    ary = [1,2]
    ary = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(ary)


