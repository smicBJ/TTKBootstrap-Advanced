import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):
    def __init__(self):
        super().__init__()
        self.title("Pack Manager")
        self.geometry("300x250")

        # The naming of your widgets is very poor as they aren't all labels
        # There is an adage in programming that says: write code like an
        # angry ax murderer will have to maintain it
        self.label_1 = tb.Label(self, text="Username", bootstyle=PRIMARY)
        self.label_2 = tb.Entry(self, bootstyle=PRIMARY)
        self.label_3 = tb.Label(self, text="Password", bootstyle=PRIMARY)
        self.label_4 = tb.Entry(self, bootstyle=PRIMARY)
        self.label_5 = tb.Button(self, text="Submit", style='Outline.TButton')

        self.label_1.pack(anchor="w", padx=15, pady=15)
        self.label_2.pack(fill=X, anchor="w", padx=15)
        self.label_3.pack(anchor="w", padx=15, pady=15)
        self.label_4.pack(fill=X, anchor="w", padx=15)
        self.label_5.pack(padx=15, pady=15, anchor="e")


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
