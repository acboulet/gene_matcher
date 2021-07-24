class CodonTarget:
    """
    Data storage class to more easily track a specific codon within the game board when searching for matches.
    """

    codon: str
    loc1: list([int, int])
    loc2: list([int, int])
    loc3: list([int, int])

    def __init__(self, codon: str, loc1: list([int, int]), loc2: list([int, int]), loc3: list([int, int])) -> None:
        self.codon = codon
        self.loc1 = loc1
        self.loc2 = loc2
        self.loc3 = loc3

    def to_string(self) -> str:
        final = self.codon + " L1:" + \
            str(self.loc1[0]) + "," + str(self.loc1[1])
        final += " L2:" + str(self.loc2[0]) + "," + str(self.loc2[1])
        final += " L3:" + str(self.loc3[0]) + "," + str(self.loc3[1])
        return (final)
