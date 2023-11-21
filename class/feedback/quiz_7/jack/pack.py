import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        self.title("Pack Manager")
        self.geometry("300x250")

        self.label_Username = tb.Label(
            self,
            text="Username",
            padding=15,
        )
        self.entry = tb.Entry(
            self,
        )
        self.Password = tb.Label(
            self,
            text="Password",
            padding=15,
        )
        self.entry_2 = tb.Entry(
            self,
        )
        self.Submit = tb.Button(
            self,
            text="Submit"
        )

        # Since you just need to anchor it to the left in a top to bottom pack, W would work just fine as the value
        # of anchor
        self.label_Username.pack(anchor=NW)
        self.entry.pack(anchor=NW, padx=15, fill=X)
        self.Password.pack(anchor=NW)
        self.entry_2.pack(anchor=NW, padx=15, fill=X)
        self.Submit.pack(anchor=NE, padx=15, pady=20)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
