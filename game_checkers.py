import json

class CheckersGame:
    def __init__(self):
        self.board = [
            [" ", "B", " ", "B", " ", "B", " ", "B"],
            ["B", " ", "B", " ", "B", " ", "B", " "],
            [" ", "B", " ", "B", " ", "B", " ", "B"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["W", " ", "W", " ", "W", " ", "W", " "],
            [" ", "W", " ", "W", " ", "W", " ", "W"],
            ["W", " ", "W", " ", "W", " ", "W", " "]
        ]
        self.current_player = "W"

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 17)

    def to_json(self):
        return json.dumps({
            "board": self.board,
            "current_player": self.current_player
        })

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        if piece == " " or piece[0] != self.current_player:
            print("Invalid move. Select a valid piece.")
            return False

        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = " "
            self.switch_player()
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        # Add logic to check if the move is valid for the current player
        # This is a basic implementation and you may need to enhance it for capturing and king movements.
        return True

    def switch_player(self):
        self.current_player = "W" if self.current_player == "B" else "B"


# Введення команд гравця
def player_input():
    try:
        start_row = int(input("Enter the start row: "))
        start_col = int(input("Enter the start column: "))
        end_row = int(input("Enter the end row: "))
        end_col = int(input("Enter the end column: "))
        return start_row, start_col, end_row, end_col
    except ValueError:
        print("Invalid input. Please enter integers.")
        return None

# Головний код гри
if __name__ == "__main__":
    game = CheckersGame()

    while True:
        game.display_board()
        
        move = player_input()
        if move:
            game.move_piece(*move)