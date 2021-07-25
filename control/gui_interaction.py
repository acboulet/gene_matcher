from tkinter import Frame, Label, PanedWindow, Tk
from tkinter.constants import BOTH, VERTICAL
from visual.matcher_gui import MatcherGui
# from visual.display_gui import DisplayGui

# root = Tk()
# root.title("Interaction")
# root.geometry("600x600")


class InteractionGui():
    complete_panel: PanedWindow  # The entire game window
    display_panel: PanedWindow  # The display window split into two
    # display_gui: DisplayGui  # The gui for displaying interaction
    match_panel: PanedWindow  # The
    matcher_gui: MatcherGui  # The gui for displaying matching pairs
    left_label: Label

    def __init__(self, root) -> None:
        game_frame = Frame(root)

        self.complete_panel = PanedWindow(
            game_frame, bd=4, relief="raised", bg="red")
        self.complete_panel.pack(fill=BOTH, expand=1)

        self.left_label = Label(self.complete_panel,
                                text="Left Panel", width=5)
        self.complete_panel.add(self.left_label)

        self.display_panel = PanedWindow(
            self.complete_panel, orient=VERTICAL, bd=4, relief="raised", bg="blue", width=500)
        self.complete_panel.add(self.display_panel)

        self.top = Label(self.display_panel, text="Top panel")
        self.display_panel.add(self.top)

        self.matcher_gui = MatcherGui(self.display_panel)
        # self.display_panel.add(self.matcher_gui)

        # self.bottom = Label(self.display_panel, text="Bottom panel")
        # self.display_panel.add(self.bottom)

        self.right_label = Label(
            self.complete_panel, text="Right Panel", width=5)
        self.complete_panel.add(self.right_label)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    # root = Tk()
    # root.title("Interaction")
    # root.geometry("600x600")
    gui = InteractionGui(root)
    root.mainloop()
