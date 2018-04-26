# Design a Tic-tac-toe game that is played between two players on a n x n grid.

# You may assume the following rules:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

# TicTacToe toe = new TicTacToe(3);

# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# Follow up:
# Could you do better than O(n2) per move() operation?

"""
Run time: 78 ms
Idea is to find a way to tell if a player wins.
This solution uses arrays of dictionaries for each row and column.
And two additional dictionaries to track diagnal progress.
If player 1 moves in row 2, we look for player one in the dictionary in row 2. The only way for player 1 to win
is to have count == n in row 2. If the dictionary is not empty, and player 1 is not in the dictionary, that means
player 2 also placed a move in row 2, and player 1 won't win this row anymore. Therefore, we don't need to check
for the case if player is not in the dict.

Same idea applied for 4 win conditions: all of one row, all of one column, diagnal from top right to bottom left,
and bottom left to top right. 
For top left to bottom right diagnals, row == col.
For bottom left to top right diagnals, row + col == n-1.
"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.col_arr = [{} for _ in range(n)]
        self.row_arr = [{} for _ in range(n)]
        self.topleft = {}
        self.bottomleft = {}
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        
        # row
        if len(self.row_arr[row]) == 0:
            self.row_arr[row][player] = 1
        else:
            if player in self.row_arr[row]:
                self.row_arr[row][player] += 1
                if self.row_arr[row][player] == self.n:
                    return player
        # col  
        if len(self.col_arr[col]) == 0:
            self.col_arr[col][player] = 1
        else:
            if player in self.col_arr[col]:
                self.col_arr[col][player] += 1
                if self.col_arr[col][player] == self.n:
                    return player
                
        # top left to bottom right
        if row == col:
            if len(self.topleft) == 0:
                self.topleft[player] = 1
            else:
                if player in self.topleft: 
                    self.topleft[player] += 1
                    if self.topleft[player] == self.n: 
                        return player

        # bottom left to top right
        if row + col == self.n - 1:
            if len(self.bottomleft) == 0:
                self.bottomleft[player] = 1
            else:
                if player in self.bottomleft: 
                    self.bottomleft[player] += 1
                    if self.bottomleft[player] == self.n: return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)