# @before-stub-for-debug-begin
from python3problem236 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

'''
    #use recursion
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            print(root.val) 
        if not root or root==p or root==q: 
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root
'''
class Solution:
    def __init__(self):
        self.result=[]
        self.dic={}
        self.vis={}

    def dfs(self,root):
        if root.left:
            self.dic[root.left.val] = root
            self.dfs(root.left)
        if root.right:
            self.dic[root.right.val] = root
            self.dfs(root.right)

    #use hash & dfs
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root)
        while p:
            self.vis[p.val] = 1
            p = self.dic.get(p.val)
        while q:
            if self.vis.get(q.val) == 1: return q
            q = self.dic.get(q.val)
        
        return none

        
# @lc code=end

