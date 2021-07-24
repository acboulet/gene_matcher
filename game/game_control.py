from game import board, game_rules
# import board, game_rules


class GameControl():

    def __init__(self) -> None:
        self.board = board.GameBoard()
        self.rules = game_rules.GameRules()

    def spots_adjacent(self, user_picks: list([[int, int], [int, int]])) -> bool:
        """
        Purpose:
            Checks the base locations on the GameBoard to ensure they're adjacent
        Precond:
            :param user_picks: list where [0] is first location and [1] is second location
                                first integer is the row, and second is the column
        Return:
            True if spaces are adjacent, False otherwise
        """
        first = user_picks[0]
        second = user_picks[1]
        # first possibility is row value is same, and col is +/- 1
        if (first[0] == second[0]) and (abs(first[1] - second[1]) == 1):
            return True
        # second possibility is col value is same, and row is +/- 1
        elif (first[1] == second[1]) and (abs(first[0] - second[0]) == 1):
            return True
        return False

    def valid_codon(self, potential_codons: list([str])):
        """
        Purpose:
            Checks a list of potential codons to see if it matches the game's target
        Precond:
            :param potential_codons: List of 4 potential codons
                                        [0] horizontal codon from first position
                                        [1] vertical codon from first position
                                        [2] horizontal codon from second position
                                        [3] vertical codon from second position
        Return:
            A string corresponding to which of the 4 codons matched
            Or None if none of them match
        """
        target = self.rules.get_codon()
        if target == potential_codons[0] or target[::-1] == potential_codons[1]:
            return "hor1"
        elif target == potential_codons[1] or target[::-1] == potential_codons[1]:
            return "ver1"
        elif target == potential_codons[2] or target[::-1] == potential_codons[2]:
            return "hor2"
        elif target == potential_codons[3] or target[::-1] == potential_codons[3]:
            return "ver2"
        else:
            return None

    def check_turn(self, user_picks: list([[int, int], [int, int]])) -> bool:
        new_board = self.game_board.copy()
        # Select the two bases, and switch them
        base_1 = new_board[user_picks[0][0]][user_picks[0][1]]
        base_2 = new_board[user_picks[1][0]][user_picks[1][1]]
        holder = base_1
        base_1 = base_2
        base_2 = holder

        possible_codons = []
        for choice in user_picks:
            possible_codons.extend(new_board.po)


# TODO create a function that deletes replaces the base pairs that match
# TODO create a function that checks the board to make sure the codon is there
# TODO creeate a function that resets the board if above function doesn't return true
if __name__ == "__main__":
    # test for spots_adjacent()
    test = GameControl()
    selection = [[4, 4], [5, 5]]
    result = test.spots_adjacent(selection)
    if (result != False):
        print("spots_adjacent() fails when spots are not adjacent")

    selection = [[4, 4], [4, 5]]
    result = test.spots_adjacent(selection)
    if (result != True):
        print("spots_adjacent() fails when rows are adjacent")

    selection = [[4, 4], [5, 4]]
    result = test.spots_adjacent(selection)
    if (result != True):
        print("spots_adjacent() fails when cols are adjacent")

    result = test.valid_codon(["ATG", "ACC", "GTA", "LOL"])
    if (result != "hor1"):
        print("valid_codon() does not find hor1")

    result = test.valid_codon(["AGG", "ACC", "GTA", "ATG"])
    if (result != "ver2"):
        print("valid_codon() does not find ver2")

    result = test.valid_codon(["AGG", "ACC", "GTA", "ACG"])
    if (result != None):
        print("valid_codon() does not return None")

    print("TESTING DONE")
