
# Explanation

  # Do a DFS of the grid for rows and cols.
  # Keep track of visited cells to not travel again


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])

        def find(r, c, w, seen):
        	if not w: return True
        	if (r, c) in seen or r == rows or r < 0 or c == cols or c < 0 or board[r][c] != w[0]: return False
        	seen.add((r, c))
        	return any([find(r+1, c, w[1:], set(seen)), find(r-1, c, w[1:], set(seen)), find(r, c+1, w[1:], set(seen)), find(r, c-1, w[1:], set(seen))])

        return any([board[r][c] == word[0] and find(r, c, word, set()) for r in xrange(rows) for c in xrange(cols)])

print Solution().exist()
