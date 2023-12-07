import ttkbootstrap as tb
from ttkbootstrap.constants import *
from K import *

class SearchBar(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)
        self.entry = tb.Entry(self)
        self.button = tb.Button(self, text='Search')

        self.entry.pack(side=LEFT,fill=X,expand=True)
        self.button.pack(side=RIGHT)

class ButtonGroup(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_button = tb.Button(self, text='submit', bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text='cancel', bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT)
        self.cancel_button.pack(side=RIGHT)


class App(tb.Window):
    def __init__(self):
        super().__init__(themename='darkly')

        self.geometry('1920x1080')
        self.subtitle = tb.Label(self, font=H1,text='SMIC RECORDS')
        self.subtitle_2 = tb.Label(self, text='Subtitle')
        self.search = SearchBar(self)

        self.subtitle_3 = tb.Label(self, text='No Search Entry')
        # self.button = tb.Button(self, text='Submit', bootstyle='SUCCESS')

        self.subtitle.pack(padx=10, pady=10, anchor=W)

        self.subtitle_2.pack(padx=10, pady=10, anchor=W)
        # self.textbox.pack(padx=10, fill=X)
        self.search.pack()
        self.subtitle_3.pack(padx=10,expand=True)
        #self.button.pack(padx=10, expand=True, anchor=E)
        self.button_group = ButtonGroup(self)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
