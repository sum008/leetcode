#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        def solve(cur_exp):
            i, start, res = 0, 0, 0
            opt = ""
            while i < len(cur_exp):
                if cur_exp[i] in ("+", "-"):
                    opt = cur_exp[i]
                    if cur_exp[i+1] == "(":
                        count = 1
                        i += 2
                        start = i
                        while count != 0:
                            i += 1
                            if cur_exp[i] == "(":
                                count += 1
                            elif cur_exp[i] == ")":
                                count -= 1
                        s = cur_exp[start:i]
                        r = solve(s)
                        if opt in ("+", ""):
                            res += r
                        else:
                            res -= r
                        opt = ""
                    else:
                        found = False
                        for j in range(0, len(cur_exp[i+1:])):
                            if cur_exp[i+1:][j] in ("+", "-"):
                                found = True
                                break
                        if not found:
                            if opt in ("+", ""):
                                res += int(cur_exp[i+1:])
                            else:
                                res -= int(cur_exp[i+1:])
                        else:
                            if opt in ("+", ""):
                                res += int(cur_exp[i+1:i+j+1])
                            else:
                                res -= int(cur_exp[i+1:i+j+1])
                        i += j+1
                        opt = cur_exp[i]
                elif cur_exp[i] == "(":
                    count = 1
                    i += 1
                    start = i
                    while count != 0:
                        i += 1
                        if cur_exp[i] == "(":
                            count += 1
                        elif cur_exp[i] == ")":
                            count -= 1
                    s = cur_exp[start:i]
                    r = solve(s)
                    if opt in ("+", ""):
                        res += r
                    else:
                        res -= r
                    opt = ""
                else:
                    found = False
                    for j in range(0, len(cur_exp[i:])):
                        if cur_exp[i:][j] in ("+", "-"):
                            found = True
                            break
                    if not found:
                        if opt in ("", "+"):
                            res += int(cur_exp[i:])
                        else:
                            res -= int(cur_exp[i:])
                    else:
                        if opt in ("", "+"):
                            res += int(cur_exp[i:i+j])
                        else:
                            res -= int(cur_exp[i:i+j])
                    i += j
                    opt = cur_exp[i]

                i += 1
            return res
        s = s.replace(" ", "")
        return solve(s)
        
# @lc code=end

