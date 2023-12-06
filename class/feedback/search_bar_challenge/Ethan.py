import ttkbootstrap as tb
from ttkbootstrap.constants import *
import K

class ButtonGroup(tb.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(padx=K.PM, pady=K.PM, fill=X)

        self.submit = tb.Button(self, text="cancel", padding=10, bootstyle=DANGER)

        self.cancel = tb.Button(self, text="submit", padding=10, bootstyle=SUCCESS)
        self.submit.pack(side=RIGHT)
        self.cancel.pack(side=RIGHT)

class searchBar(tb.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(padx=K.PM, fill=X)
        self.searchBar = tb.Entry(self)

        self.search = tb.Button(self, text="Search")

        self.searchBar.pack(side=LEFT,fill=X,expand=True)
        self.search.pack(side=RIGHT)


class App(tb.Window):

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Frames")

        self.title = tb.Label(
            self,
            text="SMIC RECORDS",
            font=K.DISPLAY4,
            padding=10,

        )
        subtitle = "Subtitle!!!"
        # appearance of 2nd label
        self.subtitle = tb.Label(
            self,
            textvariable=subtitle,
            font=K.H1,
            padding=10,


        )
        self.searchResult = tb.Label(self,
                                text="No return query"
                               )

        self.search = searchBar()

        self.title.pack(anchor=NW)
        self.subtitle.pack(anchor=NW)

        self.search.pack()
        self.searchResult.pack(expand=TRUE, fill=BOTH)
        self.Buttongroup = ButtonGroup(self)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()

