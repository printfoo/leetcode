"""
Inplace solution for Game of Life, Time O(n*m) Space O(1).

Idea:
Use difference values to represent difference conditions.
Unchanged 0: 0
Unchanged 1: 1
1 to 0: 2
0 to 1: -2

When computing, consider original value
Finally, consider real value and map back
"""

# Solution.
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def updateBoard(i, j):
            # add neighbors
            neighbors = []
            if i > 0: neighbors.append(board[i - 1][j])
            if i < len_board - 1: neighbors.append(board[i + 1][j])
            if j > 0: neighbors.append(board[i][j - 1])
            if j < wid_board - 1: neighbors.append(board[i][j + 1])
            if i > 0 and j > 0: neighbors.append(board[i - 1][j - 1])
            if i > 0 and j < wid_board - 1: neighbors.append(board[i - 1][j + 1])
            if j > 0 and i < len_board - 1: neighbors.append(board[i + 1][j - 1])
            if i < len_board - 1 and j < wid_board - 1: neighbors.append(board[i + 1][j + 1])
            living = sum([1 if n > 0 else 0 for n in neighbors])
            # update living or dead
            if board[i][j] == 1 and (living < 2 or living > 3): return 2
            elif board[i][j] == 0 and living == 3: return -2
            else: return board[i][j]

        len_board = len(board)
        wid_board = len(board[0])
        for i in range(len_board):
            for j in range(wid_board):
                board[i][j] = updateBoard(i, j)
        for i in range(len_board):
            for j in range(wid_board):
                board[i][j] = 1 if board[i][j] in {1, -2} else 0
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
