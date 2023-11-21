import ttkbootstrap as tb
from ttkbootstrap.constants import *


class App(tb.Window):

    def __init__(self):
        super().__init__()

        self.title('Unit 6 Quiz')
        self.geometry('300x250')
        self.textbox = tb.Entry(self)
        # spaces dont belong between paramaters and values
        self.subtitle = tb.Label(self, text = 'Username', bootstyle = PRIMARY)
        self.textbox_2 = tb.Entry(self)
        self.subtitle_2 = tb.Label(self, text = 'Pasword', bootstyle = PRIMARY)

        self.button_two=tb.Button(self, text='Submit',bootstyle=SUCCESS)

        # -1: the paramaters required to have at least 10 padding on the outer edges
        # side is not required with TOP because that is the default
        # -1: Missing the anchor to have them line up on the left
        # -1: Missing the fill to make it all expand the whole screen
        self.subtitle.pack(padx=5, pady=10, side = TOP)
        self.textbox.pack(padx=5, pady=10)
        self.subtitle_2.pack(padx=5, pady=10, side=TOP)
        self.textbox_2.pack(padx=5, pady=10)
        self.button_two.pack(padx=5,pady=10,side=BOTTOM)


if __name__=='__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
