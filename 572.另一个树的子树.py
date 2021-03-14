# @before-stub-for-debug-begin
from python3problem572 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,root_a,root_b):
        if not root_a and not root_b:
            return True
        if not root_a or not root_b:
            return False
        return root_a.val == root_b.val and self.isSameTree(root_a.left, root_b.left) and self.isSameTree(root_a.right, root_b.right)
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        A = self.isSameTree(s,t) 
        B = self.isSubtree(s.left,t) 
        C = self.isSubtree(s.right,t)
        return A or B or C

        
        
# @lc code=end

