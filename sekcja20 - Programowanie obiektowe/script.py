from rocket import Rocket, RocketBoard

board = RocketBoard(12)
board[0].x = 4

print(board.get_distance(board[0], board[1]))
print(len(board))
