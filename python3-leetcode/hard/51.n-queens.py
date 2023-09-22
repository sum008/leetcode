#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def driver(config):
            for i in range(0, n):
                find_valid_boards(
                    0, i, 0, ["."*i + "Q" + "."*(n-(i+1))], config)

        def valid(row, column, conf):
            for r, c in conf:
                if c == column:
                    return False
                if abs(r-row) == abs(c-column):
                    return False
            return True

        def find_valid_boards(row, column, queen_count, cur_config, conf):
            if row >= n or column >= n or row < 0 or column < 0:
                return
            # check if valid position
            if not valid(row, column, conf):
                return

            conf.append([row, column])

            # found one valid configuration
            if queen_count == n-1:
                res.append(cur_config)

            for col in range(0, n):

                find_valid_boards(row+1, col, queen_count+1,
                                  cur_config+["."*col + "Q" + "."*(n-(col+1))], conf)
            conf.pop()

        res = []
        if n == 2 or n == 3:
            return res
        if n == 1:
            return [["Q"]]
        valid_config = []
        driver(valid_config)
        return res


# @lc code=end
