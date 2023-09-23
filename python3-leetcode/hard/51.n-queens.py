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
                x = find_valid_boards(
                    0, i, 0, ["."*i + "Q" + "."*(n-(i+1))], ["."*((n-1)-i) + "Q" + "."*(n-(((n-1)-i)+1))], config)
                if x:
                    return True

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

        def find_valid_boards(row, column, queen_count, cur_config, mirror_config, conf):
            if row >= n or column >= n or row < 0 or column < 0:
                return False
            # check if valid position
            if not valid(row, column, conf):
                return False
            # found valid position
            conf.append([row, column])
            # found one valid configuration
            if queen_count == n-1:
                if len(res) == 0:
                    res.append(cur_config)
                    res.append(mirror_config)
                    temp_config.append(conf.copy())
                else:
                    if not mirror_found(conf, temp_config[0]):
                        res.append(cur_config)
                        res.append(mirror_config)
                        temp_config[0] = conf.copy()
                    else:
                        return True
            for col in range(0, n):
                # check if upcoming position is valid or not, if not then continue
                if col == column or col-1 == column or col+1 == column:
                    continue
                x = find_valid_boards(row+1, col, queen_count+1,
                                      cur_config+["."*col +
                                                  "Q" + "."*(n-(col+1))],
                                      mirror_config +
                                      ["."*((n-1)-col) + "Q" + "." *
                                       (n-(((n-1)-col)+1))],
                                      conf)
                if x:
                    return True
            conf.pop()
            return False

        res = []
        if n == 2 or n == 3:
            return res
        if n == 1:
            return [["Q"]]
        valid_config = []
        temp_config = []
        driver(valid_config)
        return res


# @lc code=end
