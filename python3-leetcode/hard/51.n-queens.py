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

        # def valid(row, column, conf):
        #     # check up:
        #     for i in range(row-1, -1, -1):
        #         if str(i)+str(column) in conf:
        #             return False
        #     # check diagonal left:
        #     i, j = row-1, column-1
        #     while i >= 0 and j >= 0:
        #         if str(i)+str(j) in conf:
        #             return False
        #         i -= 1
        #         j -= 1

        #     # check diagonal right:
        #     i, j = row-1, column+1
        #     while i >= 0 and j < n:
        #         if str(i)+str(j) in conf:
        #             return False
        #         i -= 1
        #         j += 1
        #     return True

        def valid(row, column, conf):

            for r, c in conf.keys():
                # check down in conf - increase row only
                for i in range(r+1, row+1):
                    if i == row and c == column:
                        return False
                # check down-diagonal left
                i, j = r+1, c-1
                while i < row+1 and j >= column-1:
                    if i == row and j == column:
                        return False
                    i += 1
                    j -= 1

                # check down-diagonal right
                i, j = r+1, c+1
                while i < row+1 and j < column+1:
                    if i == row and j == column:
                        return False
                    i += 1
                    j += 1
            return True

        def find_valid_boards(row, column, queen_count, cur_config, conf):
            if row >= n or column >= n or row < 0 or column < 0:
                return
            # check if valid position
            if not valid(row, column, conf):
                return

            conf[tuple([row, column])] = 1

            # found one valid configuration
            if queen_count == n-1:
                res.append(cur_config)

            for col in range(0, n):

                find_valid_boards(row+1, col, queen_count+1,
                                  cur_config+["."*col + "Q" + "."*(n-(col+1))], conf)
            conf.popitem()

        res = []
        if n == 2 or n == 3:
            return res
        if n == 1:
            return [["Q"]]
        valid_config = {}
        driver(valid_config)
        return res


# @lc code=end
