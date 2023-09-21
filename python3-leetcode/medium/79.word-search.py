#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    # find first character of the word in grid
    def exist(self, board: List[List[str]], word: str) -> bool:
        def first_word(n_row, n_col):
            # check if count of characters(appering in word) in grid is greater than length of word
            word_map = {}
            for i in range(0, n_row):
                for j in range(0, n_col):
                    if board[i][j] not in word_map:
                        word_map[board[i][j]] = 1
                    else:
                        word_map[board[i][j]] = word_map[board[i][j]]+1

            count = 0
            for i in (set(word)):
                if i in word_map:
                    count += word_map[i]
            if count < len(word):
                return False

            # find first character of the word
            for row in range(0, n_row):
                for column in range(0, n_col):
                    if board[row][column] == word[0]:
                        if search_word(row, column, n_row, n_col,
                                       0, ""):
                            return True
            return False

        # find remaining words
        def search_word(row, column, n_row, n_col, cur_word_index, cur_word):
            found = False
            if row >= n_row or column >= n_col or row < 0 or column < 0 or cur_word_index >= len(word):
                return False
            if board[row][column] != word[cur_word_index]:
                return False
            if cur_word_index == len(word)-1:
                return True
            board[row][column] = 0
            found = search_word(row-1, column, n_row, n_col, cur_word_index+1, cur_word+word[cur_word_index]) or search_word(row+1, column, n_row, n_col, cur_word_index+1, cur_word+word[cur_word_index]) or search_word(
                row, column+1, n_row, n_col, cur_word_index+1, cur_word+word[cur_word_index]) or search_word(row, column-1, n_row, n_col, cur_word_index+1, cur_word+word[cur_word_index])
            board[row][column] = word[cur_word_index]
            return found

        col = len(board[0])
        row = len(board)
        if row*col < len(word):
            return False
        return first_word(row, col)

# @lc code=end
