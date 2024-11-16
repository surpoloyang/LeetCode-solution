#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (74.80%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 84.3K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
# 
# 
# 例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
# 
# 
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
# 
# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,0,1,0,1,0,1]
# 输出：22
# 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 示例 2：
# 
# 
# 输入：root = [0]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在 [1, 1000] 范围内
# Node.val 仅为 0 或 1 
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
import typing
class Solution:
    def __init__(self) -> None:
        # self.orders = [0] * 31
        self.res = []
        self.sums = []
        # self.path = []
    def sumRootToLeaf(self, root: typing.Optional[TreeNode]) -> int:
        self.backtrack([], root)
        for lst in self.res:
            self.sums.append(self.path2sum(lst))
        return sum(self.sums)
        
    def backtrack(self, path:typing.List[TreeNode], root):
        if root is None:
            # if self.path not in self.res:
            #     self.res.append(self.path)
                
            return
            
        
        path.append(root)
        if not root.left and not root.right:
            self.res.append(list(path))
            path.pop()
        else:
            self.backtrack(path, root.left)
            self.backtrack(path, root.right)
            path.pop()
        
    def path2sum(self, lst: typing.List[TreeNode]) -> int:
        s = 0
        for i in range(len(lst)):
            s += lst[i].val * 2**(len(lst)-i-1)
        return s
    
# class Solution:
#     def sumRootToLeaf(self, root: [TreeNode]) -> int:
#         def sumRootToLeaf(root, res): # here; "res" is "sum"
#             if root == None: return 0
#             res = (2 * res) + root.val
#             if root.left == None and root.right == None: return res
#             return sumRootToLeaf(root.left, res) + sumRootToLeaf(root.right, res)
        
#         return sumRootToLeaf(root, 0)

# @lc code=end

