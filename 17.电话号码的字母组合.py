#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (60.79%)
# Likes:    2951
# Dislikes: 0
# Total Accepted:    982.9K
# Total Submissions: 1.6M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# 示例 2：
# 
# 
# 输入：digits = ""
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：digits = "2"
# 输出：["a","b","c"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
# 
# 
#

# @lc code=start
import typing
class Solution:
    def __init__(self) -> None:
        self.dic = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
            
        }
    def letterCombinations(self, digits: str) -> typing.List[str]:
        if digits == '':
            return []
        res = []
        path = []
        
        def backtrack(digits:str, path:typing.List[str], key: int):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            
            for i in range(len(self.dic[digits[key]])):
                path.append(self.dic[digits[key]][i])
                
                backtrack(digits, path, key+1)
                path.pop()
        backtrack(digits, path, 0)
        return res
    
"""
25/25 cases passed (0 ms)
Your runtime beats 100 % of python3 submissions
Your memory usage beats 57.33 % of python3 submissions (16.4 MB)
"""
# @lc code=end

