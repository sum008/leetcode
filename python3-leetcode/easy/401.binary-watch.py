#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # h = 3, m = 5
        def solve(i, index, s, r, ti, lis, t):
            if i >= ti:
                if t=="hr":
                    hr_lis.append(s)
                else:
                    mi_lis.append(s)
                return
            while index < len(lis):
                if (t == "hr" and s+lis[index] <= 11) or (t == "mi" and s+lis[index] <= 59):
                    solve(i+1, index+1, s+lis[index], r, ti, lis, t)
                index += 1

        h = [8, 4, 2, 1]
        m = [32, 16, 8, 4, 2, 1]
        if turnedOn == 0:
            return ["0:00"]
        elif 1 <= turnedOn < 9:
            res = []
            for i in range(0, turnedOn+1):
                if turnedOn-i < 6 and i < 4:
                    hr = i
                    mi = turnedOn-i
                    hr_lis=[]
                    mi_lis=[]
                    solve(0, 0, 0, [], hr, h, "hr")
                    solve(0, 0, 0, [], mi, m, "mi")
                    for h_i in hr_lis:
                        for m_i in mi_lis:
                            res.append(f'{h_i}:{str(m_i).rjust(2,"0")}')
            return res
        else:
            return []

# @lc code=end
