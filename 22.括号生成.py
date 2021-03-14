# @before-stub-for-debug-begin
from python3problem22 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        para=[]
        def backtrack(S,left,right):
            if len(S) == 2*n:
                para.append(''.join(S))
                return
            if left<n:
                S.append('(')
                backtrack(S,left+1,right)
                S.pop()

            if right<left:
                S.append(')')
                backtrack(S,left,right+1)
                S.pop()

        backtrack([],0,0)
        return para
# @lc code=end

