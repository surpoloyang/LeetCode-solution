#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
# https://leetcode.cn/problems/binary-watch/description/
#
# algorithms
# Easy (63.07%)
# Likes:    436
# Dislikes: 0
# Total Accepted:    80.6K
# Total Submissions: 127.7K
# Testcase Example:  '1'
#
# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或
# 1，最低位在右侧。
# 
# 
# 例如，下面的二进制手表读取 "4:51" 。
# 
# 
# 
# 
# 给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。
# 
# 小时不会以零开头：
# 
# 
# 例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
# 
# 
# 分钟必须由两位数组成，可能会以零开头：
# 
# 
# 例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：turnedOn = 1
# 输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# 
# 
# 示例 2：
# 
# 
# 输入：turnedOn = 9
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= turnedOn <= 10
# 
# 
#

# @lc code=start
import typing
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> typing.List[str]:
        if turnedOn > 8:
            return []
        self.nums = [1,2,4,8,1,2,4,8,16,32]
        self.visited = [0] * len(self.nums)
        self.res = []
        self.backtrack(turnedOn, 0, 0)
        return self.res
        
    def backtrack(self, turnedOn: int, step: int, start: int)-> typing.List[str]:
        if step == turnedOn:
            self.res.append(self.int2time())
            return
        
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            self.h, self.m = self.cal()
            if self.h > 11 or self.m > 59:
                self.visited[i] = 0
                continue
            
            self.backtrack(turnedOn, step+1, i+1)
            self.visited[i] = 0
            
    def cal(self, )->tuple:
        h, m = 0, 0
        for i in range(len(self.nums)):
            if self.visited[i]:
                if i < 4:
                    h += self.nums[i]
                else:
                    m += self.nums[i]
        return h, m
    
    def int2time(self, ) -> str:
        self.h, self.m = self.cal()
        if self.m < 10:
            return str(self.h) + ':0' + str(self.m)
        else: return str(self.h) + ':' + str(self.m)
                
# @lc code=end

