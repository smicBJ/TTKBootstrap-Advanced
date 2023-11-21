import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))

        # -1: Why are you using frames? This shouldn't require a frame
        # So you made it overly complex for no reason
        container = ttk.Frame(self)
        container.pack(fill=X, expand=True, pady=5)

        # -1: You don't need width
        self.label_one = ttk.Label(container, text="Username", width=10)        
        ent_1 = ttk.Entry(master=container)
        self.label_two = ttk.Label(container, text="Password", width=10)
        ent_2 = ttk.Entry(master=container)

        # -2: Second label and entry are not properly placed on the screen
        # -2: Spacing around the edge and the spacing around the widgets does not meet paramater guidelines
        self.label_one.pack(fill=X, padx=10, pady=10)
        ent_1.pack(side=LEFT, pady=15, fill=X, expand=YES)
        self.label_two.pack(fill=X, padx=10, pady=10)
        ent_2.pack(side=LEFT, padx=15, fill=X, expand=YES)


class App(ttk.Window):

    def __init__(self, theme):
        super().__init__("TTK Quiz", themename=theme)

        self.geometry("300x250")

        self.button = ttk.Button(self, text="Submit", bootstyle=(SUCCESS))

        self.button.pack(padx=15, pady=15, side=RIGHT, anchor=SE)

        self.container = ttk.Frame(self)
        self.container.pack(side=LEFT, anchor=N)

        self.frames = {
            "home": MainFrame(self.container)
        }

        self.set_frame("home")

    def set_frame(self, name):
        self.current_frame = name
        self.frames[name].pack(side=LEFT, anchor=N)


if __name__ == '__main__':
    app = App(theme="lumen")
    app.place_window_center()
    app.mainloop()