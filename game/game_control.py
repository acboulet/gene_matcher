from game import board, game_rules

class GameControl(board.GameBoard, game_rules.GameRules):

    board: board.GameBoard
    rules: game_rules.GameRules

    def __init__(self) -> None:
        self.board= board.GameBoard()
        self.rules = game_rules.GameRules()

    def valid_codon():
        #TODO is the user input codon, a match
        return None