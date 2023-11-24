import ttkbootstrap as tb
from ttkbootstrap.constants import *
FONT_TITLE = ("Verdana", 20)


class App(tb.Window):

    def __init__(self):
        super().__init__()
        self.title("Unit 6 Quiz")
        self.geometry("300x250")

        # -2: Missing the entries for the labels
        # I added the input entry
        # -1: The spacing is incorrect for the amount of spacing between the widgets
        # Changed the amount of spacing
        # Added new padding spacing
        self.label_1 = tb.Label(self,text="Username", font=FONT_TITLE)
        self.label_1.pack(anchor="w", padx=15, pady=15)
        # -1: Missing the anchor argument
        #Added anchor argument for every label and entry

        self.entry_1 = tb.Entry(self, bootstyle=PRIMARY)
        self.entry_1.pack(fill=X, anchor="w", padx=15)


        self.label_2 = tb.Label(text="Password", font=FONT_TITLE)
        self.label_2.pack(anchor="w", padx=15, pady=15)

        self.entry_2 = tb.Entry(self, bootstyle=PRIMARY)
        self.entry_2.pack(fill=X, anchor="w", padx=15)




        # -1: You call submit when it isn't a function you created
        #Changed into self.button
        self.button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.button.pack(padx=20, pady=20, anchor=NE)

# -1 This class is completely unnecessary
# I deleted the whole class


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
