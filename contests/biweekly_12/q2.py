from __future__ import annotations
import collections

# Solution.
class Leaderboard:

    def __init__(self):
        self.leader_board = collections.Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.leader_board[playerId] += score

    def top(self, K: int) -> int:
        return sum(v for _, v in self.leader_board.most_common(K))

    def reset(self, playerId: int) -> None:
        self.leader_board[playerId] = 0
        
# Main.
if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.addScore(1,73)   # leaderboard = [[1,73]];
    leaderboard.addScore(2,56)   # leaderboard = [[1,73],[2,56]];
    leaderboard.addScore(3,39)   # leaderboard = [[1,73],[2,56],[3,39]];
    leaderboard.addScore(4,51)   # leaderboard = [[1,73],[2,56],[3,39],[4,51]];
    leaderboard.addScore(5,4)    # leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
    print(leaderboard.top(1))    # returns 73;
    leaderboard.reset(1)         # leaderboard = [[2,56],[3,39],[4,51],[5,4]];
    leaderboard.reset(2)         # leaderboard = [[3,39],[4,51],[5,4]];
    leaderboard.addScore(2,51)   # leaderboard = [[2,51],[3,39],[4,51],[5,4]];
    print(leaderboard.top(3))    # returns 141 = 51 + 51 + 39;
