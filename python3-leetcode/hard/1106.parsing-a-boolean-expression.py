#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def solve(exp):
            index = 0
            bool_vals = set()
            i = 0
            while i < len(exp):
                if exp[i] in ("&", "|", "!"):
                    x, y = solve(exp[i+1:])
                    if exp[i] == "&":
                        if len(x) == 2:
                            x = {"f"}
                    elif exp[i] == "|":
                        if len(x) == 2:
                            if "t" in x:
                                x = {"t"}
                            else:
                                x = {"f"}
                    elif exp[i] == "!":
                        if "t" in x:
                            x = {"f"}
                        else:
                            x = {"t"}
                    i = i+y+1
                    index = i
                    bool_vals.update(x)
                elif exp[i] in ("t", "f"):
                    index = i
                    bool_vals.add(exp[i])
                elif exp[i] == ")":
                    index = i
                    return bool_vals, i
                i += 1
            return bool_vals, index
        a, b = solve(expression)
        a = list(a)[0]
        return True if a == "t" else False

# @lc code=end
