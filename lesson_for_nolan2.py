import ttkbootstrap as tb
from helpers.K import *


class App(tb.Window):
    def __init__(self):
        super().__init__()

        self.title("TTKBootstrap with Classes")
        self.geometry("1280x720")

        self.f_label = tb.Label(self, text="First Label", bootstyle=(INVERSE, PRIMARY), font=H3, padding=PM)
        self.s_label = tb.Label(self, text="Second Label", bootstyle=(INVERSE, WARNING), font=H3, padding=PM)

        self.f_label.pack()
        self.s_label.pack()


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
