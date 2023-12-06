import ttkbootstrap as tb
from ttkbootstrap.constants import *
from k import *

class ButtonGroup(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT,padx=(PM, 0), pady=PM)
        self.cancel_button.pack(side=RIGHT)

class SearchBar(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, fill=X)

        self.input = tb.Entry(self, bootstyle=PRIMARY, font=BODY)
        self.search = tb.Button(self, text="Search", bootstyle=(SECONDARY))

        self.search.pack(side=RIGHT, padx=(PS, 0))
        self.input.pack(side=RIGHT, expand=True, fill=X, pady=10)


class App(tb.Window):
    def __init__(self, theme):
        super().__init__(themename=theme)
        self.title("frames")
        self.geometry("1080x720")
        self.label_1 = tb.Label(self, text="SMIC RECORDS", bootstyle=PRIMARY, font=H1)
        self.label_2 = tb.Label(self, text="A great tool for searching academic records and failures", bootstyle=SECONDARY, font=("Roboto", 19, "bold"))
        self.label_4 = tb.Label(self, bootstyle="inverse-secondary", text="                                            No Query Given", font=BODY)

        self.label_1.pack(anchor="w", padx=50)
        self.label_2.pack(anchor="w", padx=50)
        self.Searchbar = SearchBar(self)
        self.label_4.pack(fill=BOTH, expand=True, padx=(50, 100), pady=(10, 100))
        self.button_group = ButtonGroup(self)


if __name__ == '__main__':
    app = App(theme="cyborg")
    app.place_window_center()
    app.mainloop()
