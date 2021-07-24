from tkinter import Tk, Button


class MatcherGui():
    # All buttons to use
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
        self.master = master
        master.title("sample")

        current_row = 1
        current_col = 1
        self.b11 = Button(text=str(current_row) + ":" + str(current_col))
        self.b11.grid(row=current_row, column=current_col)

        current_col += 1
        self.b12 = Button(text=str(current_row) + ":" + str(current_col))
        self.b12.grid(row=current_row, column=current_col)

        current_col += 1
        self.b13 = Button(text=str(current_row) + ":" + str(current_col))
        self.b13.grid(row=current_row, column=current_col)

        current_col += 1
        self.b14 = Button(text=str(current_row) + ":" + str(current_col))
        self.b14.grid(row=current_row, column=current_col)

        current_col += 1
        self.b15 = Button(text=str(current_row) + ":" + str(current_col))
        self.b15.grid(row=current_row, column=current_col)

        current_col += 1
        self.b16 = Button(text=str(current_row) + ":" + str(current_col))
        self.b16.grid(row=current_row, column=current_col)

        current_col += 1
        self.b17 = Button(text=str(current_row) + ":" + str(current_col))
        self.b17.grid(row=current_row, column=current_col)

        current_col += 1
        self.b18 = Button(text=str(current_row) + ":" + str(current_col))
        self.b18.grid(row=current_row, column=current_col)

        # ROW 2
        current_row = 2
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 3
        current_row = 3
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 4
        current_row = 4
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 5
        current_row = 5
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 6
        current_row = 6
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 7
        current_row = 7
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)

        # ROW 8
        current_row = 8
        current_col = 1
        self.b21 = Button(text=str(current_row) + ":" + str(current_col))
        self.b21.grid(row=current_row, column=current_col)

        current_col += 1
        self.b22 = Button(text=str(current_row) + ":" + str(current_col))
        self.b22.grid(row=current_row, column=current_col)

        current_col += 1
        self.b23 = Button(text=str(current_row) + ":" + str(current_col))
        self.b23.grid(row=current_row, column=current_col)

        current_col += 1
        self.b24 = Button(text=str(current_row) + ":" + str(current_col))
        self.b24.grid(row=current_row, column=current_col)

        current_col += 1
        self.b25 = Button(text=str(current_row) + ":" + str(current_col))
        self.b25.grid(row=current_row, column=current_col)

        current_col += 1
        self.b26 = Button(text=str(current_row) + ":" + str(current_col))
        self.b26.grid(row=current_row, column=current_col)

        current_col += 1
        self.b27 = Button(text=str(current_row) + ":" + str(current_col))
        self.b27.grid(row=current_row, column=current_col)

        current_col += 1
        self.b28 = Button(text=str(current_row) + ":" + str(current_col))
        self.b28.grid(row=current_row, column=current_col)


if __name__ == "__main__":
    root = Tk()
    gui = MatcherGui(root)
    root.mainloop()
