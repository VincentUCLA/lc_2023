#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.20%)
# Likes:    12722
# Dislikes: 252
# Total Accepted:    1.7M
# Total Submissions: 2.7M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur_lvl, new_lvl, cur_res, res = [], [], [], []
        if root == None: return res
        cur_lvl.append(root)
        while cur_lvl:
            cur = cur_lvl.pop(0)
            cur_res.append(cur.val)
            if cur.left != None: new_lvl.append(cur.left)
            if cur.right != None: new_lvl.append(cur.right)
            if not cur_lvl:
                cur_lvl = new_lvl
                res.append(cur_res)
                cur_res, new_lvl = [], []
        return res
            

        
# @lc code=end

