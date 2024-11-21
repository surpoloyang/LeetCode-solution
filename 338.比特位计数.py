#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode.cn/problems/counting-bits/description/
#
# algorithms
# Easy (78.91%)
# Likes:    1352
# Dislikes: 0
# Total Accepted:    352.9K
# Total Submissions: 447.1K
# Testcase Example:  '2'
#
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans
# 作为答案。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：[0,1,1,2,1,2]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# 
# 进阶：
# 
# 
# 很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
# 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）
# 
# 
# 
# 
#

# @lc code=start
import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        # bitcounts = []
        # for i in range(n+1):
        #     bitcounts.append(bin(i)[2:].count('1'))
        # return bitcounts
        """
        15/15 cases passed (15 ms)
        Your runtime beats 45.74 % of python3 submissions
        Your memory usage beats 28.14 % of python3 submissions (17.4 MB)
        """
        # bitcounts = []
        # for i in range(n+1):
        #     cnt = 0
        #     while i:
        #         cnt += i % 2
        #         i //= 2
        #     bitcounts.append(cnt)
        # return bitcounts
        """
        15/15 cases passed (55 ms)
        Your runtime beats 18.81 % of python3 submissions
        Your memory usage beats 9.85 % of python3 submissions (17.5 MB)
        """
        bitcounts = [0]
        for i in range(1, n+1):
            bitcounts.append(i % 2 + bitcounts[i // 2])
        return bitcounts
        """
        15/15 cases passed (3 ms)
        Your runtime beats 97.43 % of python3 submissions
        Your memory usage beats 5.34 % of python3 submissions (17.5 MB)
        """
# @lc code=end

