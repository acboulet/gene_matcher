from tkinter import Label, PanedWindow, Tk
from tkinter.constants import BOTH, VERTICAL

root = Tk()
root.title("Interaction")
root.geometry("600x600")


class InteractionGui():
    display_panel: PanedWindow
    match_panel: PanedWindow
    left_label: Label

    def __init__(self, root) -> None:
        self.display_panel = PanedWindow(bd=4, relief="raised", bg="red")
        self.display_panel.pack(fill=BOTH, expand=1)

        self.left_label = Label(self.display_panel, text="Left Panel", width=5)
        self.display_panel.add(self.left_label)

        self.panel_2 = PanedWindow(
            self.display_panel, orient=VERTICAL, bd=4, relief="raised", bg="blue", width=500)
        self.display_panel.add(self.panel_2)

        self.top = Label(self.panel_2, text="Top panel")
        self.panel_2.add(self.top)

        self.bottom = Label(self.panel_2, text="Bottom panel")
        self.panel_2.add(self.bottom)

        self.right_label = Label(
            self.display_panel, text="Right Panel", width=5)
        self.display_panel.add(self.right_label)


gui = InteractionGui(root)
root.mainloop()
