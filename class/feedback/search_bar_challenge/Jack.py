import ttkbootstrap as tb
from ttkbootstrap.constants import *
from k import *


# class ButtonGroup(tb.Frame):
#
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack(padx=PM, fill=X, pady=PM)
#
#         self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
#         self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))
#
#         self.submit_button.pack(side=RIGHT, padx=(PM, 0))
#         self.cancel_button.pack(side=RIGHT)


class SearchBar(tb.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PL, fill=X, pady=PL)

        self.search_entry = tb.Entry(self)
        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)

        self.submit_button.pack(side=RIGHT, padx=(PXS, 0))
        self.search_entry.pack(fill=X)


class App(tb.Window):

    def __init__(self):
        super().__init__(themename="minty")

        self.title("Frames")
        self.geometry("1280x720")
        self.title_label = tb.Label(self, bootstyle=PRIMARY, text="SMIC RECORDS", font=H1)
        self.subtitle_label = tb.Label(self, text="Get academic records of SMIC students", font=LEAD)
        self.result_label = tb.Label(self, text="No Query Given", font=LEAD)

        self.title_label.pack(anchor=NW, padx=PL, pady=(15, 0))
        self.subtitle_label.pack(anchor=NW, padx=PL)
        self.search_bar = SearchBar(self)
        self.result_label.pack(expand=True, padx=PL, pady=PM)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
