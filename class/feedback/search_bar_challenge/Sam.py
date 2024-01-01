import requests as req
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SearchBar(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(padx=20, pady=(0, 20), fill=X)

        self.search_bar = ttk.Entry(self)
        self.search_button = ttk.Button(self, text="Search", command=self.get_records)

        self.search_bar.pack(side=LEFT, fill=X, expand=True)
        self.search_button.pack(side=LEFT, padx=(5, 0))

    def get_records(self):
        name = self.search_bar.get()
        url_string = f"https://192.168.1.29:8000/names/{name}"
        response = req.get(url_string).json()
        print(response)


class ButtonGroup(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill=X)

        self.submit_button = ttk.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = ttk.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT, padx=(20, 0))
        self.cancel_button.pack(side=RIGHT)


class App(ttk.Window):

    def __init__(self, theme):
        super().__init__(themename=theme)

        self.title("SMIC RECORDS")
        self.geometry("1280x720")

        self.label_title = ttk.Label(self, text="SMIC RECORDS", bootstyle=PRIMARY, font=("Garamond", 39, "bold"))
        self.label_two = ttk.Label(self, text="A great tool for finding random foods completely unrelated to SMIC", bootstyle=SECONDARY, font=("Garamond", 20))
        self.results_label = ttk.Label(self, text="No query given", font=("Garamond", 16))    

        self.label_title.pack(padx=20, pady=(20, 10), anchor=W)
        self.label_two.pack(padx=20, pady=(0, 20), anchor=W)
        self.search_bar = SearchBar(self)


if __name__ == "__main__":
    app = App(theme="vapor")
    app.place_window_center()
    app.mainloop()