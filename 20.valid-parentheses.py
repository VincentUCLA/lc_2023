#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char in ["(", "[", "{"]:
                stk.append(char)
            else:
                if not stk:
                    return False
                elif char == ")":
                    if stk[-1] == "(":
                        stk.pop()
                    else:
                        return False
                elif char == "]":
                    if stk[-1] == "[":
                        stk.pop()
                    else:
                        return False
                elif char == "}":
                    if stk[-1] == "{":
                        stk.pop()
                    else:
                        return False
        if stk:
            return False
        return True
                
# @lc code=end

