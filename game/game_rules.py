
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

    print("TESTING COMPLETE")
