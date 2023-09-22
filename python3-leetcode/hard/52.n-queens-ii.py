#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def driver(config):
            for i in range(0, n):
                find_valid_boards(
                    0, i, 0, config)

        def valid(row, column, conf):
            for r, c in conf:
                if c == column or abs(r-row) == abs(c-column):
                    return False
            return True

        # def check_prev_pos(cur_row, cur_col, prev_row, prev_col):
        #     if cur_col == prev_col or (cur_row-1 == prev_row and cur_col-1 == prev_col) or (cur_row-1 == prev_row and cur_col+1 == prev_col):
        #         return False
        #     return True

        def find_valid_boards(row, column, queen_count, conf):
            if row >= n or column >= n or row < 0 or column < 0:
                return
            # check if valid position
            if not valid(row, column, conf):
                return
            # found valid position
            conf.append([row, column])
            # found one valid configuration
            if queen_count == n-1:
                res.append(1)
            for col in range(0, n):
                # check if upcoming position is valid or not, if not then continue
                if col == column or col-1 == column or col+1 == column:
                    continue
                find_valid_boards(row+1, col, queen_count+1, conf)
            conf.pop()

        res = []
        if n == 2 or n == 3:
            return 0
        if n == 1:
            return 1
        valid_config = []
        driver(valid_config)
        return len(res)

# @lc code=end
