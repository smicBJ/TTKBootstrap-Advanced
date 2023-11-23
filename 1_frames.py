import ttkbootstrap as tb
from ttkbootstrap.constants import *
from k import *


class ButtonGroup(tb.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT, padx=(PM, 0))
        self.cancel_button.pack(side=RIGHT)


class App(tb.Window):

    def __init__(self):
        super().__init__(themename="minty")

        self.title("Frames")
        self.geometry("854x640")

        subtitle = "A great tool for searching academic records and failures"

        self.title_label = tb.Label(self, bootstyle=PRIMARY, text="SMIC Academic Records", font=H1)
        self.subtitle_label = tb.Label(self, text=subtitle, font=LEAD)
        self.search_bar = tb.Entry(self, font=BODY)
        self.search_results_label = tb.Label(self, text="No query given", font=BODY)

        self.title_label.pack(anchor=W, pady=(PM, PS), padx=PM)
        self.subtitle_label.pack(anchor=W, pady=(0, PM), padx=PM)
        self.search_bar.pack(fill=X, padx=PM)
        self.search_results_label.pack(expand=True, padx=PM, pady=PM)

        self.button_group = ButtonGroup(self)
        self.button_group_1 = ButtonGroup(self)


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
