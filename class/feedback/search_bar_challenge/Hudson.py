import ttkbootstrap as tb
from ttkbootstrap.constants import *

from K import *

class ButtonGroup(tb.Frame):

    def __init__(self, massa):
        super().__init__(massa)

        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_buttom = tb.Button(self,
                                       text="Submit",
                                       bootstyle=SUCCESS
                                       )

        self.cancel_button = tb.Button(self,
                                       text="Cancel",
                                       bootstyle=(OUTLINE, SECONDARY)
                                       )

        self.submit_buttom.pack(side=RIGHT, padx=(PM, 0))

        self.cancel_button.pack(side=RIGHT)


class SearchBarGroup(tb.Frame):
    def __init__(self, massa):
        super().__init__(massa)
        self.pack(fill=X, padx=PM, pady=PM)

        self.search_entry = tb.Entry(self)

        self.submit_buttom = tb.Button(self,
                                       text="Search"
                                       )

        self.search_entry.pack(expand=True, fill=X, side=LEFT)
        self.submit_buttom.pack(side=LEFT)


class App(tb.Window):

    def __init__(self, theme):
        super().__init__(themename=theme)
        self.title("Frames")
        self.geometry("1280x720")

        self.title_label = tb.Label(text="SMIC RECORDS",
                                    font=DISPLAY4,
                                    bootstyle=PRIMARY
                                    )

        self.subtitle_label = tb.Label(text="Subtitle",
                                       font=H3
                                       )

        # self.entry = tb.Entry()

        self.query_label = tb.Label(text="No Search Query",
                                    font=H4
                                    )

        self.title_label.pack(padx=20,
                              pady=20,
                              anchor=W
                              )

        self.subtitle_label.pack(padx=30,
                                 anchor=W
                                 )

        self.search = SearchBarGroup(self)

        # self.entry.pack(expand=True,
        #                 padx=20,
        #                 pady=20,
        #                 fill=X,
        #                 anchor=N
        #                 )

        self.query_label.pack(expand=True,
                              anchor=N
                              )

        # self.button_group = ButtonGroup(self)

if __name__ == "__main__":
    app = App(theme="minty")
    app.place_window_center()
    app.mainloop()