#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def all_paranthesis(self, left_brace, right_brace, brace, cur_str, n, res):
        if right_brace > left_brace:
            return
        final_str = cur_str + brace
        if left_brace < n:
            self.all_paranthesis(left_brace+1, right_brace,
                                 "(", final_str, n, res)
        if right_brace < n:
            self.all_paranthesis(left_brace, right_brace +
                                 1, ")", final_str, n, res)
        if left_brace+right_brace == n*2:
            res.append(final_str)
            return

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.all_paranthesis(1, 0, "", "(", n, res)
        return res


# @lc code=end
