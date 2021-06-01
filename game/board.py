from random import randint

class GameBoard:
    
    # Protected variable to store Game_board
    game_board = []

    def __init__(self) -> None:
        self.new_board()

    """
    Purpose:
        Build a new 8x8 game board with a random selection of bases at each spot
        Should only be called upon initializing a new board
    Post:
        GameBoard.game_board will no longer be an empty list
    """
    @staticmethod
    def new_board():
        for n in range(8):
            row = []
            for i in range(8):
                row.append(GameBoard.random_base())
            GameBoard.game_board.append(row)

    """
    Purpose: 
        Generate a random potential DNA base
    Return:
        An individual string character
    """
    @staticmethod
    def random_base() -> str:
        bases =["A", "C", "G", "T"]
        rand_int = randint(0,3)
        return bases[rand_int]
    # check if move was successful

    """
    Purpose:
        Given a players choice of row and column values, returns the horizontal and vertical codons at that location on the board
    Pre:
        :param player_choice: row and column value choice by player (not indices)
    Return:
        List containing codons for [0] horizontal and [1] vertical options.
    """
    def possible_codons(self, player_choice: list([int, int])) -> list([str, str]):
        # TODO currently it does not ask the pieces to switch
        possible_codons = [None,None] # hor, vert
        row, col = player_choice
        # If the col value is left/right then there is no horizontal option
        if col != 1 and col != 8:
            possible_row = self.game_board[row-1]
            possible_codons[0] = possible_row[col-2] + possible_row[col-1] + possible_row[col]
        # If the row value is top or bottom, then there is no vertical option
        if row != 1 and row != 8:
            first = self.game_board[row-2][col-1]
            second = self.game_board[row-1][col-1]
            third = self.game_board[row][col-1]
            possible_codons[1] = first + second + third
        return possible_codons


    """
    Purpose:
        Output the gameboard as a String
    Return:
        The gameboard as a printable string
    """
    @staticmethod
    def to_string() -> str:
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
    result = test_board.possible_codons([1,1])
    if result != [None, None]:
        print("possible_codon selection on corner does yield None, None")
        print(result)
    
    # Print statements because of randomly generated table
    print("Test grabbing row 1 and col 4, should yield no vertical value:")
    result = test_board.possible_codons([1,4])
    print(result)
    print("Test grabbing row 4 and col 1, should yield no horizontal value:")
    result = test_board.possible_codons([4,1])
    print(result)
    print("Test grabbing row 4 and col 4, should yield center board:")
    result = test_board.possible_codons([4,4])
    print(result)


    