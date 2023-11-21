import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        # set up the package basic
        self.title("Unit 6 Quiz")
        self.geometry("300x250")
        # appearance of 1st label
        self.label_1 = tb.Label(
            self,
            text="Username",
            padding=10,
            bootstyle=()
        )

        # appearance of 2nd label
        self.label_2 = tb.Label(
            self,
            text="Password",
            padding=10,
            bootstyle=()
        )

        # Button 2 suggests there is a button 1 🙃
        self.button2 = tb.Button(self, text="submit", bootstyle=SUCCESS)
        self.box1 = tb.Entry(self)
        self.box2 = tb.Entry(self)

        self.label_1.pack(anchor=NW)
        self.box1.pack(padx=10, pady=10, anchor=NW, expand=TRUE, fill=X)
        self.label_2.pack(anchor=NW)
        self.box2.pack(padx=10, pady=10, anchor=NW, expand=TRUE, fill=X)

        # -1: This is the only one that is missing the padding
        self.button2.pack(padx=4, pady=10, anchor=S, side=RIGHT)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
