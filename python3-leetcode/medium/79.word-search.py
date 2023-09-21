#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_word(row, column, n_row, n_col, cur_word_index, cur_word, initial):
            if row >= n_row or column >= n_col or row < 0 or column < 0 or cur_word_index >= len(word):
                return
            if initial == "i":
                while row < n_row:
                    column = 0
                    while column < n_col:
                        if board[row][column] == word[0]:
                            search_word(row, column, n_row, n_col,
                                        cur_word_index, cur_word, "")
                            if len(res) > 0:
                                return
                        column += 1
                    row += 1

            else:
                if board[row][column] != word[cur_word_index]:
                    return
                board[row][column] = '1'
                search_word(row-1, column, n_row, n_col,
                            cur_word_index+1, cur_word+word[cur_word_index], "")
                search_word(row+1, column, n_row, n_col,
                            cur_word_index+1, cur_word+word[cur_word_index], "")
                search_word(row, column+1, n_row, n_col,
                            cur_word_index+1, cur_word+word[cur_word_index], "")
                search_word(row, column-1, n_row, n_col,
                            cur_word_index+1, cur_word+word[cur_word_index], "")
                board[row][column] = word[cur_word_index]
                if cur_word+word[cur_word_index] == word:
                    res.append(1)
                    return

        col = len(board[0])
        row = len(board)
        res = []
        if row*col < len(word):
            return False
        search_word(0, 0, row, col, 0, "", "i")
        if len(res) > 0:
            return True
        return False


# @lc code=end
