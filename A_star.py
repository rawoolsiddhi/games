import time

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def heuristic(board, target):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != target[i][j]:
                count += 1
    return count

def apply_move(board, move):
    x, y = find_zero(board)
    dx, dy = move
    nx, ny = x + dx, y + dy
    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
    return board, (nx, ny)

def main():
    input_board = [[0] * 3 for _ in range(3)]
    target_board = [[0] * 3 for _ in range(3)]

    print("Enter the start and end configurations:")
    for i in range(3):
        for j in range(3):
            input_board[i][j] = int(input(f"Input board [{i}][{j}]: "))
            target_board[i][j] = int(input(f"Target board [{i}][{j}]: "))

    print("\nInitial configuration:")
    print_board(input_board)
    
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    current_board = [row[:] for row in input_board]
    while current_board != target_board:
        h = heuristic(current_board, target_board)
        print("Heuristic:", h)
        print("Current configuration:")
        print_board(current_board)
        time.sleep(2)
        print("---------------------")
        print("\nselected!!!\n")
        for move in moves:
            if 0 <= find_zero(current_board)[0] + move[0] < 3 and 0 <= find_zero(current_board)[1] + move[1] < 3:
                new_board, new_zero = apply_move([row[:] for row in current_board], move)
                new_h = heuristic(new_board, target_board)
                print("Heuristic for move", move, ":", new_h)
                print("Resulting configuration after applying move:")
                print_board(new_board)
                time.sleep(3)
        current_board = new_board

if __name__ == "__main__":
    main()
