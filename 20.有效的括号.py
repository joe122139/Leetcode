#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) ==0:
            return True
        # use stack
        stk=[]
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stk.append(c)
            elif (c==')' or c==']' or c=='}') and len(stk)==0:
                return False
            elif c==')':
                re = stk.pop()
                if(re!='('):
                    return False
            elif c==']':
                re = stk.pop()
                if re!='[':
                    return False
            elif c=='}':
                re = stk.pop()
                if re!='{':
                    return False
        if(len(stk)==0):
            return True
        else:
            return False
# @lc code=end

