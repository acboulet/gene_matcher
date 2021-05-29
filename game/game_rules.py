
class GameRules:
    sequence: str
    current_location: int

    def __init__(self) -> None:
        self.sequence = "ATGAACTGA"
        self.current_location = 0

    """
    Purpose:
        Checks if the player has won the game
    Return:
        True if player has won, False otherwise
    """
    def game_won(self) -> bool:
        return (self.current_location + 3 == len(self.sequence))

    """
    Purpose:
        Moves selector to next codon section
    Post cond:
        self.current_location has moved forward 3
    """
    def next_codon(self) -> None:
        self.current_location = self.current_location + 3

    """
    Purpose:
        Grabs next codon in the sequence
    Return:
        3-length string with current targetted codon
    """
    def return_codon(self) -> str:
        return (self.sequence[self.current_location: self.current_location+3])


# Used for testing
if __name__ == "__main__":
    test = GameRules()
    
    # Initial test for game_won(), next_codon(), and return_codon()
    if test.game_won() != False:
        print("game_won() not working without any turns")
    if test.current_location != 0:
        print("self.current_location is not set properly at start")
    if test.return_codon() != "ATG":
        print("return_codon() does not return correct sequence at turn 0")
    
    # move forward 1 codon, and test again
    test.next_codon()
    if test.game_won() != False:
        print("game_won() not working on turn 1")
    if test.current_location != 3:
        print("self.current_location is not working on turn 1")
    if test.return_codon() != "AAC":
        print("return_codon() does not return correct sequence at turn 1")

    # move forward to last codon, and test again  
    test.next_codon()
    if test.game_won() != True:
        print("game_won() not working on last turn")
    if test.current_location != 6:
        print("self.current_location is not working on last turn")
    if test.return_codon() != "TGA":
        print("return_codon() does not return correct sequence on last codon")

    print("TESTING COMPLETE")
