#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {x: idx for idx, x in enumerate(nums)}
        for idx, x in enumerate(nums):
            if target - x in dic:
                if idx == dic[target - x]:
                    continue
                return [idx, dic[target - x]]
        
# @lc code=end

