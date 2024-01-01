import ttkbootstrap as tb
from helpers.K import *


class App(tb.Window):
    def __init__(self, theme):
        super().__init__(themename=theme)

        self.title("TTKBootstrap with Classes")
        self.geometry("1280x720")

        self.f_label = tb.Label(self, text="First Label", bootstyle=(INVERSE, PRIMARY), font=H3, padding=PM)
        self.s_label = tb.Entry(self)
        self.t_label = tb.Button(self, text="Submit")

        # padx/y, ipadx/ipady, side, expand, fill, anchor
        self.f_label.pack()
        self.s_label.pack()
        self.t_label.pack()


if __name__ == '__main__':
    app = App(theme="sandstone")
    app.place_window_center()
    app.mainloop()