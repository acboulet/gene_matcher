from tkinter import Tk
from control.gui_interaction import InteractionGui


if __name__ == "__main__":
    root = Tk()
    root.title("Gene Matcher")
    root.geometry("600x600")

    game = InteractionGui(root)
    root.mainloop()
