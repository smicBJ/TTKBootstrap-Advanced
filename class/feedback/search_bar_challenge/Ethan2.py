import ttkbootstrap as tb
from ttkbootstrap.constants import *
from K import *
 # import requests as req

class ButtonGroup(tb.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT, padx=(PM, 0))
        self.cancel_button.pack(side=RIGHT)



class searchBar(tb.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)
        self.searchBar = tb.Entry(self)

        self.search = tb.Button(self, text="Search", commnad=self.search_for_record())

        self.searchBar.pack(side=LEFT,fill=X,expand=True)
        self.search.pack(side=LEFT)

    def search_for_record(self):
        name = "乐子人"
        url_string = f"http://10.6.21.76:8000/names/{name}"
#       res = req.get(url_string)



class App(tb.Window):

    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Frames")

        self.title = tb.Label(
            self,
            text="SMIC RECORDS",
            font=DISPLAY4,


        )
        subtitle = "Subtitle!!!"
        # appearance of 2nd label
        self.subtitle = tb.Label(
            self,
            textvariable=subtitle,
            font=H1,



        )
        self.searchResult = tb.Label(self,
                                text="No return query"
                               )

        #self.search = searchBar(self)

        self.title.pack(padx=20,
                              pady=20,
                              anchor=W)
        self.subtitle.pack(padx=30,
                                 anchor=W)

        # self.search.pack(anchor=W, pady=(0, PM), padx=PM)
        self.search = searchBar(self)
        self.searchResult.pack(expand=True,
                              anchor=N)
        self.Buttons = ButtonGroup(self)
        #self.button_group = ButtonGroup(self)
        #self.button_group_1 = ButtonGroup(self)

if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()

