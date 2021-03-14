# @before-stub-for-debug-begin
from python3problem98 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
            
        
    def isValidBST(self, root: TreeNode) -> bool:
        def traverse(root, up,dn):
            if root:
                if dn< root.val < up:
                    v_left= traverse(root.left,root.val,dn)
                    v_right= traverse(root.right,up,root.val)
                    if (v_left and v_right) == False:
                        return False
                else:
                    return False
            return True

        isValid = traverse(root,float('inf'),float('-inf'))

        return isValid
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
#   ary = ["eat","tea","tan","ate","nat","bat"]
    ary = [2,1,3]
    print(s.isValidBST(ary))

