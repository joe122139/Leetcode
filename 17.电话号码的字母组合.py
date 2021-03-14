# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        result=[]
        temp=[]
        if not digits:
            return result
        for dig in digits:
            if dic.get((dig)):
                temp.append(dic.get((dig)))
        
        def dfs(s,temp):
            if not temp:
                result.append(s)
                return
            for i in temp[0]:
                dfs(s+i,temp[1:])
        
        dfs('',temp)
        return result
        



# @lc code=end

