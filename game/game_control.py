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

    def valid_codon(self, potential_codons):
        """
        Purpose:
            Checks a list of potential codons to see if it matches the game's target
        Precond:
            :param potential_codons: List of potential codons from game_rules.possible_codons
                                        [0] string for codon
                                        [1] [int, int] for location of first base
                                        [2] [int, int] for location of second base
                                        [3] [int, int] for location of third base
        Return:
            The codon from the list of potential codons, that is a match
            Or None if none of them match
        """
        target = self.rules.get_codon()
        # Check each codon in the potential list
        for codon in potential_codons:
            # if the string matches the target sequence, then return the entire codon item
            if target == codon[0] or target.__reversed__ == codon[0]:
                return codon
        return None

    def check_user_choices(self, user_picks: list([[int, int], [int, int]])) -> tuple([bool, list]):
        """
        Purpose:
            Checks if user selection matches the target codon
        Precond:
            :param user_picks: list where [0] is first location and [1] is second location
                                first integer is the row, and second is the column
        Return: True if user codon matches the codon target, false otherwise
                And the codon format as per game_rules.possible_codons()
        """
        # Create a new board where you have switched the two user choices
        new_board = self.game_board.copy()
        base_1 = new_board[user_picks[0][0]][user_picks[0][1]]
        base_2 = new_board[user_picks[1][0]][user_picks[1][1]]
        holder = base_1
        base_1 = base_2
        base_2 = holder

        possible_codons = []
        for choice in user_picks:
            possible_codons.extend(
                self.rules.possible_codons(choice, new_board))
        codon_match = self.valid_codon(possible_codons)
        if codon_match != None:
            self.board.game_board = new_board
            return (True, codon_match)
        else:
            return (False, codon_match)
            # TODO update this to now work with console_interaction
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
