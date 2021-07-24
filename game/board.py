from random import randint


class GameBoard:

    # Protected variable to store Game_board
    game_board = []

    def __init__(self) -> None:
        self.new_board()

    @staticmethod
    def new_board():
        """
        Purpose:
            Build a new 8x8 game board with a random selection of bases at each spot
            Should only be called upon initializing a new board
        Post:
            GameBoard.game_board will no longer be an empty list
        """
        for n in range(8):
            row = []
            for i in range(8):
                row.append(GameBoard.random_base())
            GameBoard.game_board.append(row)

    @staticmethod
    def random_base() -> str:
        """
        Purpose: 
            Generate a random potential DNA base
        Return:
            An individual string character
        """
        bases = ["A", "C", "G", "T"]
        rand_int = randint(0, 3)
        return bases[rand_int]

    def possible_codons(self, player_choice: list([int, int])) -> list([str, str]):
        """
        Purpose:
            Given a players choice of row and column values, returns the horizontal and vertical codons at that location on the board
        Pre:
            :param player_choice: row and column value choice by player (not indices)
        Return:
            List containing codons for [0] horizontal and [1] vertical options.
        """
        # TODO currently it does not ask the pieces to switch
        possible_codons = [None, None]  # hor, vert
        row, col = player_choice
        # If the col value is left/right then there is no horizontal option
        if col != 1 and col != 8:
            possible_row = self.game_board[row-1]
            possible_codons[0] = possible_row[col-2] + \
                possible_row[col-1] + possible_row[col]
        # If the row value is top or bottom, then there is no vertical option
        if row != 1 and row != 8:
            first = self.game_board[row-2][col-1]
            second = self.game_board[row-1][col-1]
            third = self.game_board[row][col-1]
            possible_codons[1] = first + second + third
        return possible_codons

    def possible_codon_v2(self, player_choices: list([int, int])):
        """
        Purpose:
            Given a players choice of row and column values, return all possible codons originating from that spot
        Pre:
            :param player_choice: row and column value choice by player (not indices)
        Return:
            List of every possible codon. Each item as follows:
                [0] : String for codon
                [1] : [int, int] for location of first base
                [2] : [int, int] for location of second base
                [3] : [int, int] for location of third base
        """
        row_index = player_choices[0] - 1
        col_index = player_choices[1] - 1

        codons = []

        # move along the row, and grab each three-base codon
        # if reaching the end of the board (col = 6) or user choice then stop
        col = col_index - 2  # -2 to find starting base
        # If more than index 6 (column 7) then cannot grab 3 bases
        while col < 6 and col <= col_index:
            if col >= 0:
                # [ codon, h:v1, h:v2, h:v3]
                codon = []
                first = self.game_board[row_index][col]
                second = self.game_board[row_index][col+1]
                third = self.game_board[row_index][col+2]
                seq = first + second + third
                codon.append(seq)
                codon.append([row_index + 1, col+1])
                codon.append([row_index + 1, col+2])
                codon.append([row_index + 1, col+3])
                codons.append(codon)
            col += 1

         # move down the column, and grab each three-base codon
        # if reaching the end of the board (row = 6) or user choice then stop
        row = row_index - 2
        while row < 6 and row <= row_index:
            if row >= 0:
                # [ codon, h:v1, h:v2, h:v3]
                codon = []
                first = self.game_board[row][col_index]
                second = self.game_board[row + 1][col_index]
                third = self.game_board[row + 2][col_index]
                seq = first + second + third
                codon.append(seq)
                codon.append([row + 1, col_index + 1])
                codon.append([row + 2, col_index + 1])
                codon.append([row + 3, col_index + 1])
                codons.append(codon)
            row += 1

        return codons

    @staticmethod
    def to_string() -> str:
        """
        Purpose:
            Output the gameboard as a String
        Return:
            The gameboard as a printable string
        """
        output = "Gameboard: \n"
        for line in GameBoard.game_board:
            for base in line:
                output += base + " "
            output += "\n"
        return output


if __name__ == "__main__":
    test_board = GameBoard()
    # test_board.new_board()
    print(test_board.to_string())

    # Test of possible_codons()
    # First test is a corner which should yield no results
    result = test_board.possible_codons([1, 1])
    if result != [None, None]:
        print("possible_codon selection on corner does yield None, None")
        print(result)

    # # Print statements because of randomly generated table
    # print("Test grabbing row 1 and col 4, should yield no vertical value:")
    # result = test_board.possible_codons([1,4])
    # print(result)
    # print("Test grabbing row 4 and col 1, should yield no horizontal value:")
    # result = test_board.possible_codons([4,1])
    # print(result)
    # print("Test grabbing row 4 and col 4, should yield center board:")
    # result = test_board.possible_codons([4,4])
    # print(result)
    # print("")

    # Print statements testing possible_codon_helper
    print("Testing grabbing from center with v2")
    result = test_board.possible_codon_v2([4, 4])
    print(result)
    print("Testing grabbing from left with v2")
    result = test_board.possible_codon_v2([4, 1])
    print(result)
    print("Testing grabbing from right with v2")
    result = test_board.possible_codon_v2([4, 8])
    print(result)
    print("Testing grabbing from top with v2")
    result = test_board.possible_codon_v2([1, 4])
    print(result)
    print("Testing grabbing from bottom with v2")
    result = test_board.possible_codon_v2([8, 4])
    print(result)
    print("Testing grabbing from top corner with v2")
    result = test_board.possible_codon_v2([1, 1])
    print(result)
    print("Testing grabbing from bottom with v2")
    result = test_board.possible_codon_v2([8, 8])
    print(result)
