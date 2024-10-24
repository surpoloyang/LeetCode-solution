#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#
# https://leetcode.cn/problems/sqrtx/description/
#
# algorithms
# Easy (38.63%)
# Likes:    1592
# Dislikes: 0
# Total Accepted:    970.5K
# Total Submissions: 2.5M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 4
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        left = 0
        right = x//2
        while left <= right:
            mid = (right-left)//2 + left
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                right = mid-1
            else:
                left = mid+1
        return -1
# @lc code=end

