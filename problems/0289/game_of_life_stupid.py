"""
Stupid solution for Game of Life, Time O(n*m) Space O(n*m).

Idea:
Copy and compute
"""

# Solution.
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def updateBoard(b, i, j):
            # add neighbors
            neighbors = []
            if i > 0: neighbors.append(b[i - 1][j])
            if i < len_board - 1: neighbors.append(b[i + 1][j])
            if j > 0: neighbors.append(b[i][j - 1])
            if j < wid_board - 1: neighbors.append(b[i][j + 1])
            if i > 0 and j > 0: neighbors.append(b[i - 1][j - 1])
            if i > 0 and j < wid_board - 1: neighbors.append(b[i - 1][j + 1])
            if j > 0 and i < len_board - 1: neighbors.append(b[i + 1][j - 1])
            if i < len_board - 1 and j < wid_board - 1: neighbors.append(b[i + 1][j + 1])
            living = sum(neighbors)
            # update living or dead
            if b[i][j] == 1 and (living < 2 or living > 3): return 0
            elif b[i][j] == 0 and living == 3: return 1
            else: return b[i][j]

        len_board = len(board)
        wid_board = len(board[0])
        b = [row[:] for row in board]
        for i in range(len_board):
            for j in range(wid_board):
                board[i][j] = updateBoard(b, i, j)
        return

# Main.
if __name__ == "__main__":
    board = [
     [0,1,0],
     [0,0,1],
     [1,1,1],
     [0,0,0]
     ]
    print(Solution().gameOfLife(board))
