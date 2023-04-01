#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (70.69%)
# Likes:    9601
# Dislikes: 311
# Total Accepted:    1.2M
# Total Submissions: 1.7M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= numRows <= 30
# 
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        else:
            lastPascal = self.generate(numRows - 1)
            currPascal = [1]
            for p in range(1, len(lastPascal[-1])):
                currPascal.append(lastPascal[-1][p - 1] + lastPascal[-1][p])
            currPascal.append(1)
            lastPascal.append(currPascal)
            return lastPascal

# @lc code=end

