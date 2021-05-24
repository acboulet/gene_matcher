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