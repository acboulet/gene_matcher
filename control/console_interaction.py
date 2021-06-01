from game import game_control


class ConsolePlay:

    def __init__(self) -> None:
        self.control = game_control.GameControl()
        
    """
    Purpose:
        Runs the game in the console.
    """
    def run(self):
        while not self.control.rules.game_won():
            self.start_turn()
            user_values = self.take_turn()
            # Check turn
            possible_codons = self.control.board.possible_codons(user_values)
            print(user_values)
            print(possible_codons)


    """
    Purpose:
        Print the required information for the start of a turn
    """
    def start_turn(self):
        print("Here is the current board:")
        print(self.control.board.to_string())
        print("Here is the current sequence:")
        target_seq = self.control.rules.get_sequence()
        target_seq[1] = "\033[1m" + target_seq[1] + "\033[0m"
        if target_seq[0] == None:
            print(target_seq[1] + "_" +  target_seq[2])
        elif target_seq[2] == None:
            print(target_seq[0] + "_" + target_seq[1])
        else:
            print(target_seq[0] + "_" + target_seq[1] + "_" + target_seq[2])
        print("") # empty line

    """
    Purpose:
        Handles console input for each turn.
    Return:
        A list where [0] is the row selected, and [1] is the column
    """
    def take_turn(self) -> list([[int, int], [int, int]]):
        user_values =[[None, None], [None, None]]
        correct = False # Ensure the two spaces selected are adjacent
        while not correct:
            for n in range(2):
                print("Select base %i to switch" % (n+1))
                print("Please select a row:", end=" ")
                user_values[n][0] = self.user_pick_spot()
                print("Please select a col:", end=" ")
                user_values[n][1] = self.user_pick_spot()
            
            if self.control.spots_adjacent(user_values):
                correct = True
            else:
                print("Bases are not adjacent in square. Try again")
        return user_values

    """
    Purpose:
        Accept a single digit from the console and return as int.
    Return:
        An integer between 1-8 corresponding to the game board
    """
    def user_pick_spot(self) -> int:
        accepted = False
        while(not accepted):
            val = str(input(">"))
            if val.isdigit() and (1 <= int(val)) and (int(val) <= 8):
                accepted = True
                return int(val)
            else:
                print("Input was not correct. Try again.")