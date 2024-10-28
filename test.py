class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major = nums[0]
        cnt = 1
        for i in nums[1:]:
            if i != major:
                cnt -= 1
                if cnt == 0:
                    major = i
            else:
                cnt += 1
        return major
    
Solution().majorityElement([3,2,3])