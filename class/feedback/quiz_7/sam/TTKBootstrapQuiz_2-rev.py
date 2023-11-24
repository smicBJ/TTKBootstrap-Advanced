import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# My recomendation moving forward is to not use things I have not taught as it leads to overcomplicating
# the task at hand... like using frames when I did not show you all how to properly use it

# i was sleeping........................... i cloned ur repo before the quiz started and was looking at 3_frames.py
# the second one i went to ttkbootstrap's website and got one of their sample files....
# class MainFrame(ttk.Frame):
#     def __init__(self, master):
#         super().__init__(master, padding=(10, 10))

#         self.Username = ttk.StringVar(value="")
#         self.Password = ttk.StringVar(value="")

#         self.create_form_entry("Username", self.Username)
#         self.create_form_entry("Password", self.Password)

#     def create_form_entry(self, label, variable):
#         container = ttk.Frame(self)
#         container.pack(fill=X, expand=YES, pady=15)

#         # -1: Width is not required
#         lbl = ttk.Label(master=container, text=label.title(), width=10)
#         lbl.pack(anchor=W, pady=10, padx=10, fill=X)

#         ent = ttk.Entry(master=container, textvariable=variable)
#         ent.pack(anchor=W, pady=10, padx=10, fill=X, expand=YES)

# removed redundancy

class App(ttk.Window):

    def __init__(self, theme):
        super().__init__("TTK Quiz", themename=theme)

        self.geometry("300x250")

        # self.container = ttk.Frame(self)

        # -1 This is packed from the wrong side
        # -1 As a result, the widgets are not in the correct places
        # self.container.pack(side=LEFT, anchor=N)

        # self.frames = {
        #     "home": MainFrame(self.container)
        # }

        # self.set_frame("home")

        # -1: because all the complications, the spacing is all over the place
        self.label_0 = ttk.Label(self, text="Username")
        self.entry_0 = ttk.Entry(self)
        self.label_1 = ttk.Label(self, text="Password")
        self.entry_1 = ttk.Entry(self)
        self.button = ttk.Button(self, text="Submit", bootstyle=(SUCCESS))

        self.label_0.pack(padx=15, pady=15, anchor=W)
        self.entry_0.pack(padx=10, pady=10, fill=X, anchor=W)
        self.label_1.pack(padx=15, pady=15, anchor=W)
        self.entry_1.pack(padx=10, pady=10, fill=X, anchor=W)
        self.button.pack(padx=15, pady=15, anchor=SE)

    # def set_frame(self, name):
    #     self.current_frame = name
    #     self.frames[name].pack(side=LEFT, anchor=N)

if __name__ == '__main__':
    app = App(theme="lumen")
    app.place_window_center()
    app.mainloop()