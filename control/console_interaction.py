from game.board import GameBoard


class ConsolePlay:

    def __init__(self) -> None:
        self.board= GameBoard()


    def run(self):
        # While the game has not completed, run.
        print(self.board.to_string())
        values = ConsolePlay.user_pick_spot()
        print(values)


    """
    Purpose:
        Accept two numbers from console input that correspond to row and column values
        in the game board.
    Return:
        A list where the first item is the row and second int is column
    """
    @staticmethod
    def user_pick_spot() -> list([int, int]):
        accepted = False
        while(not accepted):
            print("Please select a row and column.")
            user_values = str(input(">"))
            user_values = [int(user_values[0]), int(user_values[1])]
            # Veryify user values are within accepted values
            # TODO: build function to check user input, include if it is any corner
            if len(user_values) == 2 and (0 <= user_values[0] and user_values[0] <= 7) and (0 <= user_values[1] and user_values[1] <= 7):
                accepted = True
                return 
            

        