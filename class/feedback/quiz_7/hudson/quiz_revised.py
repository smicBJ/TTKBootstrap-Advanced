import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        self.title("Unit 6 Quiz")
        self.geometry("300x250")

        self.user_label = tb.Label(
            self,
            text="Username",
            # padding=10,
            bootstyle=(PRIMARY)
        )

        self.user_entry = tb.Entry(
            self,
            bootstyle=(PRIMARY)
        )
        self.pass_label = tb.Label(
            self,
            text="Password",
            # padding=10,
            bootstyle=(PRIMARY)
        )

        # Try avoiding using width as it will make the design unresponsive ✔
        self.pass_entry = tb.Entry(
            self,
            show="●",
            bootstyle=(PRIMARY)

        )

        self.submit = tb.Button(
            self,
            text="Submit",
            bootstyle=SUCCESS
        )
        # side, expand, fill, anchor, padx, pady
        self.user_label.pack(anchor=W, padx=10)
        # -1: Due to using width, you missed the opportunity to let the pack manager handle this ✔
        # you forgot about the fill option and the padx option ✔
        self.user_entry.pack(padx=10, expand=True, fill=X)
        self.pass_label.pack(padx=10, anchor=W)
        self.pass_entry.pack(padx=10, expand=True, fill=X)
        self.submit.pack(padx=20, pady=20, expand=True, anchor=E)


if __name__ == "__main__":
    app = App()
    app.place_window_center()
    app.mainloop()