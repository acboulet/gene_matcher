from game import game_control


class ConsolePlay:
    """
    Controls the gameplay and handles all user interaction through the console
    """

    def __init__(self) -> None:
        self.control = game_control.GameControl()

    def run(self):
        """
        Purpose:
            Runs the game in the console.
        """
        while not self.control.rules.game_won():
            correct_turn = False
            while not correct_turn:
                self.start_turn()
                user_values = self.take_turn()
                codon_match = self.control.check_user_choices(user_values)
                if codon_match[0]:
                    correct_turn = True
                    self.control.rules.next_codon()
                    print("> Correct codon selection.")
                else:
                    print("> Player choice of codons do not match target")
            print(user_values)
        print("You win!")

    def start_turn(self):
        """
        Purpose:
            Print the required information for the start of a turn
        """
        print("Here is the current board:")
        print(self.control.board.to_string())
        print("Here is the current sequence:")
        target_seq = self.control.rules.get_sequence()
        target_seq[1] = "\033[1m" + target_seq[1] + "\033[0m"
        if target_seq[0] == None:
            print(target_seq[1] + "_" + target_seq[2])
        elif target_seq[2] == None:
            print(target_seq[0] + "_" + target_seq[1])
        else:
            print(target_seq[0] + "_" + target_seq[1] + "_" + target_seq[2])
        print("")  # empty line

    def take_turn(self) -> list([[int, int], [int, int]]):
        """
        Purpose:
            Handles console input for each turn.
        Return:
            A list where [0] is the row selected, and [1] is the column
        """
        user_values = [[None, None], [None, None]]
        adjacent = False  # Ensure the two spaces selected are adjacent
        while not adjacent:
            for n in range(2):
                # TODO: Flip the two bases, and try to match. If not, flip back
                print("Select base %i to switch" % (n+1))
                print("Please select a row:", end=" ")
                user_values[n][0] = self.user_pick_spot()
                print("Please select a col:", end=" ")
                user_values[n][1] = self.user_pick_spot()

            if self.control.spots_adjacent(user_values):
                adjacent = True
            else:
                print("Bases are not adjacent in square. Try again")
        return user_values

    def user_pick_spot(self) -> int:
        """
        Purpose:
            Accept a single digit from the console and return as int.
        Return:
            An integer between 1-8 corresponding to the game board
        """
        accepted = False
        while(not accepted):
            val = str(input(">"))
            if val.isdigit() and (1 <= int(val)) and (int(val) <= 8):
                accepted = True
                return int(val)
            else:
                print("Input was not correct. Try again.")

    # def check_turn(self, user_picks: list([[int, int], [int, int]])) -> tuple([bool, str]):
    #     """
    #     Purpose:
    #         Checks to make sure the user selection matches the target codon.
    #     Precond:
    #         :param user_picks: list where [0] is first location and [1] is second location
    #                             first integer is the row, and second is the column
    #     Return: True if user codon matches target codon
    #             Str value corresponding to which codon matched
    #     """
    #     # For each location picked by the user, return all the potential codons attached
    #     # TODO: WILL NEED TO CHANGE THIS TO CHECK FOR POTENTIAL CODONS WHEN POSITIONS HAVE CHANGED
    #     possible_codons = []
    #     for choice in user_picks:
    #         possible_codons.extend(self.control.board.possible_codons(choice))
    #     codon_match = self.control.valid_codon(possible_codons)
    #     if codon_match != None:
    #         return (True, codon_match)
    #     return (False, codon_match)
