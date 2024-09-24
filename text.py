# Step 1: Set Up the Game Board
def create_board():
    return [" " for _ in range(9)]

# Step 2: Display the Game Board
def display_board(board):
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Step 3: Player Input
def player_input(board, player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("This position is already taken.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

# Step 4: Check for a Win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Step 5: Check for a Draw
def check_draw(board):
    return all(cell != " " for cell in board)

# Step 6: Switch Players
def switch_player(current_player):
    return "O" if current_player == "X" else "X"

# Step 7: Main Game Loop
def main():
    board = create_board()
    current_player = "X"
    while True:
        display_board(board)
        player_input(board, current_player)
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            break
        current_player = switch_player(current_player)

# Run the game
main()
