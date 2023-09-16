#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def form_unique_digits(self, index, cur_str, digits, key_pad, res):
        if index == len(digits):
            if len(cur_str) > 0:
                res.append(cur_str)
            # print(cur_str)
            return
        start = 0
        while start < len(key_pad[digits[index]]):
            final_str = cur_str+key_pad[digits[index]][start]
            self.form_unique_digits(index+1, final_str, digits, key_pad, res)
            start += 1

    def letterCombinations(self, digits: str) -> List[str]:
        key_pad = {"2": "abc", "3": "def", "4": "ghi",
                   "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.form_unique_digits(0, "", digits, key_pad, res)
        return res

# @lc code=end
