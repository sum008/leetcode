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
                x = find_valid_boards(
                    0, i, 0, config)
                if x:
                    return True
            return False

        def valid(row, column, conf):
            for r, c in conf:
                if c == column or abs(r-row) == abs(c-column):
                    return False
            return True

        def mirror_found(cur_res, prev_res):
            index = 0
            k = n-1
            for i, j in cur_res:
                if k-j != prev_res[index][1]:
                    return False
                index += 1
            return True

        def find_valid_boards(row, column, queen_count, conf):
            if row >= n or column >= n or row < 0 or column < 0:
                return False
            # check if valid position
            if not valid(row, column, conf):
                return False
            # found valid position
            conf.append([row, column])
            # found one valid configuration
            if queen_count == n-1:
                # print(conf)
                if len(res) > 0:
                    if not mirror_found(conf, res[0]):
                        counter[0] = counter[0]+1
                        res[0] = conf.copy()

                    else:
                        return True
                else:
                    counter.append(1)
                    res.append(conf.copy())
            for col in range(0, n):
                # check if upcoming position is valid or not, if not then continue
                if col == column or col-1 == column or col+1 == column:
                    continue
                x = find_valid_boards(row+1, col, queen_count+1, conf)
                if x:
                    return True
            conf.pop()
            return False

        res = []
        if n == 2 or n == 3:
            return 0
        if n == 1:
            return 1
        valid_config = []
        counter = []
        driver(valid_config)
        return counter[0]*2

# @lc code=end
