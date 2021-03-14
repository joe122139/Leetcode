# @before-stub-for-debug-begin
from python3problem199 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections as collection
class Solution:
    def __init__(self):
        self.result=[]
        self.level=[]
        self.depth=-1
    
# use BFS, get the left to right order of each node. 
# Store the last node on each level
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return self.result
        queue = collection.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
            
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            self.result.append(level[-1])
        return self.result

# use DFS, post search the rightmost node in the tree.
    def dfs_post(self,root,depth):
        if root:
            depth +=1
            if len(self.result) == depth:
                self.result.append(root.val)
            self.dfs_post(root.right,depth)
            self.dfs_post(root.left,depth)

    def rightSideView(self, root: TreeNode) -> List[int]:
        self.dfs_post(root,-1)
        return self.result


# @lc code=end

