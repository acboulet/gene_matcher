from tkinter import *

root = Tk()
root.title("Root")
root.geometry("475x500")


class MatcherGui():
    # TODO how do I return data after the button click?
    # TODO where do I store user data in future?

    # How many buttons have been clicked
    count: int = 0

    # Track the users picks where [0] is first choice, and [1] is second choice
    # nested list [0] is row and [1] is column
    user_picks = []

    # All buttons to use | row is first digit and col is second digit
    b11: Button
    b12: Button
    b13: Button
    b14: Button
    b15: Button
    b16: Button
    b17: Button
    b18: Button

    b21: Button
    b22: Button
    b23: Button
    b24: Button
    b25: Button
    b26: Button
    b27: Button
    b28: Button

    b31: Button
    b32: Button
    b33: Button
    b34: Button
    b35: Button
    b36: Button
    b37: Button
    b38: Button

    b41: Button
    b42: Button
    b43: Button
    b44: Button
    b45: Button
    b46: Button
    b47: Button
    b48: Button

    b51: Button
    b52: Button
    b53: Button
    b54: Button
    b55: Button
    b56: Button
    b57: Button
    b58: Button

    b61: Button
    b62: Button
    b63: Button
    b64: Button
    b65: Button
    b66: Button
    b67: Button
    b68: Button

    b71: Button
    b72: Button
    b73: Button
    b74: Button
    b75: Button
    b76: Button
    b77: Button
    b78: Button

    b81: Button
    b82: Button
    b83: Button
    b84: Button
    b85: Button
    b86: Button
    b87: Button
    b88: Button

    def __init__(self, master):
        button_frame = Frame(master)
        master.title("nucleotide_buttons")

        button_frame.grid(pady=10, padx=10)

        button_height = 3
        button_width = 6

        current_row = 1
        current_col = 1
        self.b11 = Button(master, text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b11, 1, 1))
        self.b11.grid(row=current_row, column=current_col)

        current_col += 1
        self.b12 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b12, 1, 2))
        self.b12.grid(row=current_row, column=current_col)

        current_col += 1
        self.b13 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b13, 1, 3))
        self.b13.grid(row=current_row, column=current_col)

        current_col += 1
        self.b14 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b14, 1, 4))
        self.b14.grid(row=current_row, column=current_col)

        current_col += 1
        self.b15 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b15, 1, 5))
        self.b15.grid(row=current_row, column=current_col)

        current_col += 1
        self.b16 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b16, 1, 6))
        self.b16.grid(row=current_row, column=current_col)

        current_col += 1
        self.b17 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b17, 1, 7))
        self.b17.grid(row=current_row, column=current_col)

        current_col += 1
        self.b18 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b18, 1, 8))
        self.b18.grid(row=current_row, column=current_col)

        # ROW 2
        current_row = 2
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b21, 2, 1))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b22, 2, 2))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b23, 2, 3))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b24, 2, 4))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b25, 2, 5))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b26, 2, 6))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b27, 2, 7))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b28, 2, 8))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 3
        current_row = 3
        current_col = 1
        self.b31 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b31, 3, 1))
        self.b31.grid(row=current_row, column=current_col)

        current_col += 1
        self.b32 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b32, 3, 2))
        self.b32.grid(row=current_row, column=current_col)

        current_col += 1
        self.b33 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b33, 3, 3))
        self.b33.grid(row=current_row, column=current_col)

        current_col += 1
        self.b34 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b34, 3, 4))
        self.b34.grid(row=current_row, column=current_col)

        current_col += 1
        self.b35 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b35, 3, 5))
        self.b35.grid(row=current_row, column=current_col)

        current_col += 1
        self.b36 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b36, 3, 6))
        self.b36.grid(row=current_row, column=current_col)

        current_col += 1
        self.b37 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b37, 3, 7))
        self.b37.grid(row=current_row, column=current_col)

        current_col += 1
        self.b38 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b38, 3, 8))
        self.b38.grid(row=current_row, column=current_col)

        # ROW 4
        current_row = 4
        current_col = 1
        self.b41 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b41, 4, 1))
        self.b41.grid(row=current_row, column=current_col)

        current_col += 1
        self.b42 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b42, 4, 2))
        self.b42.grid(row=current_row, column=current_col)

        current_col += 1
        self.b43 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b43, 4, 3))
        self.b43.grid(row=current_row, column=current_col)

        current_col += 1
        self.b44 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b44, 4, 4))
        self.b44.grid(row=current_row, column=current_col)

        current_col += 1
        self.b45 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b45, 4, 5))
        self.b45.grid(row=current_row, column=current_col)

        current_col += 1
        self.b46 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b46, 4, 6))
        self.b46.grid(row=current_row, column=current_col)

        current_col += 1
        self.b47 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b47, 4, 7))
        self.b47.grid(row=current_row, column=current_col)

        current_col += 1
        self.b48 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b48, 4, 8))
        self.b48.grid(row=current_row, column=current_col)

        # ROW 5
        current_row = 5
        current_col = 1
        self.b51 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b51, 5, 1))
        self.b51.grid(row=current_row, column=current_col)

        current_col += 1
        self.b52 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b52, 5, 2))
        self.b52.grid(row=current_row, column=current_col)

        current_col += 1
        self.b53 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b53, 5, 3))
        self.b53.grid(row=current_row, column=current_col)

        current_col += 1
        self.b54 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b54, 5, 4))
        self.b54.grid(row=current_row, column=current_col)

        current_col += 1
        self.b55 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b55, 5, 5))
        self.b55.grid(row=current_row, column=current_col)

        current_col += 1
        self.b56 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b56, 5, 6))
        self.b56.grid(row=current_row, column=current_col)

        current_col += 1
        self.b57 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b57, 5, 7))
        self.b57.grid(row=current_row, column=current_col)

        current_col += 1
        self.b58 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b58, 5, 8))
        self.b58.grid(row=current_row, column=current_col)

        # ROW 6
        current_row = 6
        current_col = 1
        self.b61 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b61, 6, 1))
        self.b61.grid(row=current_row, column=current_col)

        current_col += 1
        self.b62 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b62, 6, 2))
        self.b62.grid(row=current_row, column=current_col)

        current_col += 1
        self.b63 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b63, 6, 3))
        self.b63.grid(row=current_row, column=current_col)

        current_col += 1
        self.b64 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b64, 6, 4))
        self.b64.grid(row=current_row, column=current_col)

        current_col += 1
        self.b65 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b65, 6, 5))
        self.b65.grid(row=current_row, column=current_col)

        current_col += 1
        self.b66 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b66, 6, 6))
        self.b66.grid(row=current_row, column=current_col)

        current_col += 1
        self.b67 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b67, 6, 7))
        self.b67.grid(row=current_row, column=current_col)

        current_col += 1
        self.b68 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b68, 6, 8))
        self.b68.grid(row=current_row, column=current_col)

        # ROW 7
        current_row = 7
        current_col = 1
        self.b71 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b71, 7, 1))
        self.b71.grid(row=current_row, column=current_col)

        current_col += 1
        self.b72 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b72, 7, 2))
        self.b72.grid(row=current_row, column=current_col)

        current_col += 1
        self.b73 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b73, 7, 3))
        self.b73.grid(row=current_row, column=current_col)

        current_col += 1
        self.b74 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b74, 7, 4))
        self.b74.grid(row=current_row, column=current_col)

        current_col += 1
        self.b75 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b75, 7, 5))
        self.b75.grid(row=current_row, column=current_col)

        current_col += 1
        self.b76 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b76, 7, 6))
        self.b76.grid(row=current_row, column=current_col)

        current_col += 1
        self.b77 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b77, 7, 7))
        self.b77.grid(row=current_row, column=current_col)

        current_col += 1
        self.b78 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b78, 7, 8))
        self.b78.grid(row=current_row, column=current_col)

        # ROW 8
        current_row = 8
        current_col = 1
        self.b81 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b81, 8, 1))
        self.b81.grid(row=current_row, column=current_col)

        current_col += 1
        self.b82 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b82, 8, 2))
        self.b82.grid(row=current_row, column=current_col)

        current_col += 1
        self.b83 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b83, 8, 3))
        self.b83.grid(row=current_row, column=current_col)

        current_col += 1
        self.b84 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b84, 8, 4))
        self.b84.grid(row=current_row, column=current_col)

        current_col += 1
        self.b85 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b85, 8, 5))
        self.b85.grid(row=current_row, column=current_col)

        current_col += 1
        self.b86 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b86, 8, 6))
        self.b86.grid(row=current_row, column=current_col)

        current_col += 1
        self.b87 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b87, 8, 7))
        self.b87.grid(row=current_row, column=current_col)

        current_col += 1
        self.b88 = Button(text=str(current_row) + ":" + str(current_col),
                          height=button_height, width=button_width, command=lambda: self.button_click(self.b88, 8, 8))
        self.b88.grid(row=current_row, column=current_col)

    def button_click(self, button, row, col):
        if self.count < 2:
            # Generate user choice by observing row and column selection
            choice = [int(row), int(col)]
            self.user_picks.append(choice)
            print(choice)
            self.count += 1


gui = MatcherGui(root)
root.mainloop()
