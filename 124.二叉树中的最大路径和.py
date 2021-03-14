# @before-stub-for-debug-begin
from python3problem124 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs traverse()
    def __init__(self):
        self.max = float('-inf')

    def traverse(self,root):
        if root:
            val = root.val

            left_max = max(0,self.traverse(root.left))
            right_max = max(0,self.traverse(root.right))
            self.max = max(self.max, left_max + val + right_max)
            return val + max(left_max,right_max)
        else: return 0
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.max
# @lc code=end

