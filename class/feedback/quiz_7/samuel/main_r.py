import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        self.title('Unit 6 Quiz')
        self.geometry('400x300')

        self.textbox = tb.Entry(self, show='L')
        self.subtitle = tb.Label(self, text='Username')
        self.textbox_2 = tb.Entry(self, show='L')
        self.subtitle_2 = tb.Label(self, text='Password')
        self.button = tb.Button(self, text='Submit', bootstyle='SUCCESS')

        self.subtitle.pack(padx=10, pady=10, anchor=W)
        self.textbox.pack(padx=10, fill=X)
        self.subtitle_2.pack(padx=10, pady=10, anchor=W)
        self.textbox_2.pack(padx=10, fill=X)
        self.button.pack(padx=10, expand=True, anchor=E)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
