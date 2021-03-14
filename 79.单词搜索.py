# @before-stub-for-debug-begin
from python3problem79 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def __init__(self):
        self.flag = False

    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])

        def backtrack(ch,i,j,word,vis):
            #if already visited, return
            if vis[i][j] == True: return False
            vis[i][j] = True
            if len(word)==1 and ch==word[0]: 
                self.flag = True
                return True
            if ch == word[0]:
                if i>0:
                    backtrack(board[i-1][j],i-1,j,word[1:],vis)
                if i+1<row:
                    backtrack(board[i+1][j],i+1,j,word[1:],vis)
                if j>0:
                    backtrack(board[i][j-1],i,j-1,word[1:],vis)
                if j+1<col:
                    backtrack(board[i][j+1],i,j+1,word[1:],vis)
            vis[i][j] = False
            return False
            

        for i in range(row):
            for j in range(col):
                # backtrack each element
                ch = board[i][j]
                self.flag = False
                vis = [[False for k in range(col)] for l in range(row)]
                backtrack(ch,i,j,word,vis)
                if self.flag == True: return True
                j+=1
            i+=1
        
        return False
# @lc code=end

