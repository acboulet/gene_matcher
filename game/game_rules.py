from game.codon_target import CodonTarget
# from codon_target import CodonTarget


class GameRules:
    sequence: str
    current_location: int

    def __init__(self) -> None:
        self.sequence = "ATGAACTGA"
        self.current_location = 0

    def game_won(self) -> bool:
        """
        Purpose:
            Checks if the player has won the game
        Return:
            True if player has won, False otherwise
        """
        return (self.current_location == len(self.sequence))

    def next_codon(self) -> None:
        """
        Purpose:
            Moves selector to next codon section
        Post cond:
            self.current_location has moved forward 3
        """
        self.current_location = self.current_location + 3

    def get_codon(self) -> str:
        """
        Purpose:
            Grabs next codon in the sequence
        Precond:
            not game_won()
        Return:
            3-length string with current targetted codon
        """
        if not self.game_won():
            return (self.sequence[self.current_location: self.current_location+3])

    def get_sequence(self) -> list([str, str, str]):
        """
        Purpose:
            Get the game sequence but in three parts to make processing easier.
        Precond:
            not game_won()
        Return:
            List where [0] is upstream sequence
                        [1] is codon searching for
                        [2] is downstream sequence
        """
        sequence = [None, None, None]
        if not self.game_won():
            sequence[1] = self.get_codon()
            # If at start, then there is no upstream sequence
            if self.current_location == 0:
                sequence[2] = self.sequence[3:]
            # If at the last codon, then there is no downstream sequence
            elif self.current_location == len(self.sequence) - 3:
                sequence[0] = self.sequence[0:self.current_location]
            else:
                sequence[0] = self.sequence[0:self.current_location]
                sequence[2] = self.sequence[self.current_location +
                                            3:len(self.sequence)]
        return sequence

    def possible_codons(self, player_choice: list([int, int]), game_board):
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
        row_index = player_choice[0] - 1
        col_index = player_choice[1] - 1

        codons = []

        # move along the row, and grab each three-base codon
        # if reaching the end of the board (col = 6) or user choice then stop
        col = col_index - 2  # -2 to find starting base
        # If more than index 6 (column 7) then cannot grab 3 bases
        while col < 6 and col <= col_index:
            if col >= 0:
                # [ codon, h:v1, h:v2, h:v3]
                first = game_board[row_index][col]
                second = game_board[row_index][col+1]
                third = game_board[row_index][col+2]
                seq = first + second + third
                codon = CodonTarget(
                    seq, [row_index + 1, col+1], [row_index + 1, col+2], [row_index + 1, col+3])
                codons.append(codon)
            col += 1

         # move down the column, and grab each three-base codon
        # if reaching the end of the board (row = 6) or user choice then stop
        row = row_index - 2
        while row < 6 and row <= row_index:
            if row >= 0:
                # [ codon, h:v1, h:v2, h:v3]
                first = game_board[row][col_index]
                second = game_board[row + 1][col_index]
                third = game_board[row + 2][col_index]
                seq = first + second + third
                codon = CodonTarget(
                    seq, [row + 1, col_index + 1], [row + 2, col_index + 1], [row + 3, col_index + 1])
                codons.append(codon)
            row += 1

        return codons


        # Used for testing
if __name__ == "__main__":
    test = GameRules()

    # Initial test for game_won(), next_codon(), and return_codon()
    if test.game_won() != False:
        print("game_won() not working without any turns")
    if test.current_location != 0:
        print("self.current_location is not set properly at start")
    if test.get_codon() != "ATG":
        print("return_codon() does not return correct sequence at turn 0")
    result = test.get_sequence()
    if result != [None, "ATG", "AACTGA"]:
        print("get_sequence() not working on first turn")

    # move forward 1 codon, and test again
    test.next_codon()
    if test.game_won() != False:
        print("game_won() not working on turn 1")
    if test.current_location != 3:
        print("self.current_location is not working on turn 1")
    if test.get_codon() != "AAC":
        print("return_codon() does not return correct sequence at turn 1")
    result = test.get_sequence()
    if result != ["ATG", "AAC", "TGA"]:
        print("get_sequence() not working on second turn")

    # move forward to last codon, and test again
    test.next_codon()
    if test.game_won() != False:
        print("game_won() not working on last turn")
    if test.current_location != 6:
        print("self.current_location is not working on last turn")
    if test.get_codon() != "TGA":
        print("return_codon() does not return correct sequence on last codon")
    result = test.get_sequence()
    if result != ["ATGAAC", "TGA", None]:
        print("get_sequence() not working on last turn")

    # Test if the game was won when moving past last codon
    test.next_codon()
    if test.game_won() != True:
        print("game_won() not working at end turn")
    if test.current_location != 9:
        print("self.current_location is not working at end game")
    if test.get_codon() != None:
        print("return_codon() does not return None at end game")
    result = test.get_sequence()
    if result != [None, None, None]:
        print("get_sequence() not working at end game")

    # Print statements testing possible_codon_helper
    test_board = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],
                  ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
                  ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
                  ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
                  ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
                  ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
                  ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
                  ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"], ]
    for row in test_board:
        print(row)
    print("--")
    print("Testing grabbing from center")
    result = test.possible_codons([4, 4], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()
    print("Testing grabbing from left")
    result = test.possible_codons([4, 1], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()
    print("Testing grabbing from right")
    result = test.possible_codons([4, 8], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()
    print("Testing grabbing from top")
    result = test.possible_codons([1, 4], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()
    print("Testing grabbing from bottom")
    result = test.possible_codons([8, 4], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()
    print("Testing grabbing from top corner")
    result = test.possible_codons([1, 1], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()
    print("Testing grabbing from bottom corner")
    result = test.possible_codons([8, 8], test_board)
    for item in result:
        print(item.to_string(), end="")
        print()

    print("TESTING COMPLETE")
