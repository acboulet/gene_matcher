from tkinter import Tk, Button

root = Tk()
root.title("Display")
root.geometry("475x500")


class DisplayGui():

    def __init__(self, master):
        display_frame = Frame(master)


gui = DisplayGui(root)
root.mainloop()
