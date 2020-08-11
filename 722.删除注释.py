#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#
# author: Jianbin.Zhou
# Date: 2020/08/04

# @lc code=start
#  When finding the // begin to delete the characters until the end of List[j]
#  When finding the /* begin to delete the characters until */ is met. 

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        isDeleteRegion = False
        for j,s in enumerate(List):
            for i in len(s):
                if s[i] == '/' and s[i+1]=='/':
                    #only remove this row
                    s.pop(i)
                    s.pop(i+1)
                elif s[i]=='/' and s[i+1]=='*':
                    isDeleteRegion = True
                    if 
                    #comment block, may remove multiples rows
        
# @lc code=end

