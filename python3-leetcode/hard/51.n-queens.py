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
                temp = "."*i + "Q" + "."*(n-(i+1))
                find_valid_boards(0, i, 0, [temp], config)
                if len(config) > 0:
                    config.popitem()

        def find_valid_boards(row, column, queen_count, cur_config, conf):
            if row >= n or column >= n or row < 0 or column < 0:
                return
            # check if valid position
            # check up:
            for i in range(row-1, -1, -1):
                if tuple([i, column]) in conf:
                    return
            # check diagonal left:
            i, j = row-1, column-1
            while True:
                if i < 0 or j < 0:
                    break
                if tuple([i, j]) in conf:
                    return
                i -= 1
                j -= 1

            # check diagonal right:
            i, j = row-1, column+1
            while True:
                if i < 0 or j >= n:
                    break
                if tuple([i, j]) in conf:
                    return
                i -= 1
                j += 1

            conf[tuple([row, column])] = 1

            # found one valid configuration
            if queen_count == n-1:
                res.append(cur_config)

            for col in range(0, n):
                find_valid_boards(row+1, col, queen_count+1,
                                  cur_config+["."*col + "Q" + "."*(n-(col+1))], conf)
            conf.popitem()

        res = []
        valid_config = {}
        driver(valid_config)
        return res


# @lc code=end
