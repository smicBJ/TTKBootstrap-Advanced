import ttkbootstrap as tb
from ttkbootstrap.constants import *
class App(tb.Window):


    def __init__(self):
        super().__init__()

        self.geometry("300x250")

        self.label_1 = tb.Label(self, text="Username", padding=10, bootstyle=PRIMARY)
        self.label_2 = tb.Label(self, text="password", padding=10, bootstyle=PRIMARY)
        self.button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.input_1 = tb.Entry(self, text=None)
        self.input_2 = tb.Entry(self, text=None)

        self.label_1.pack(fill=X, anchor=E)
        # -1: Missing the fill option to make the entry go to both ends; it needs some padding once done
        self.input_1.pack()
        self.label_2.pack(fill=X, anchor=E)
        self.input_2.pack()
        self.button.pack(padx=20, pady=20, anchor=NE)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()