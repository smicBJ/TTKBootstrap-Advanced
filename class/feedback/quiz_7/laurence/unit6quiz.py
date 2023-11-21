import ttkbootstrap as tb

FONT_TITLE = ("Verdana", 20)


class App(tb.Window):

    def __init__(self, theme):
        super().__init__(themename=theme, iconphoto="logor.png")

        self.title("Unit 6 Quiz")
        self.geometry("300x250")

        # -2: Missing the entries for the labels
        # -1: The spacing is incorrect for the amount of spacing between the widgets
        self.label_1 = tb.Label(text="Username", font=FONT_TITLE)
        # -1: Missing the anchor argument
        self.label_1.pack(pady=10)

        self.label_2 = tb.Label(text="Password", font=FONT_TITLE)
        self.label_2.pack(pady=25)

        # -1: You call submit when it isn't a function you created
        self.button_1 = tb.Button(text="Submit", bootstyle="success, outline", command=self.submit)
        self.button_1.pack(pady=40)


# -1 This class is completely unnecessary
# class SearchForm(tb.Frame):
#
#     def first_widget(self, label, variable):
#         container = tb.Frame(self)
#         container.pack(fill=X, expand=YES, pady=15)
#
#         lbl = tb.Label(master=container, text=label.title(), width=15)
#         lbl.pack(side=LEFT, padx=15)
#
#         ent = tb.Entry(master=container, textvariable=variable)
#         ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
#
#
#     def second_widget(self, label, variable):
#         container = tb.Frame(self)
#         container.pack(fill=X, expand=YES, pady=35)
#
#         lbl = tb.Label(master=container, text=label.title(), width=35)
#         lbl.pack(side=LEFT, padx=35)
#
#         ent = tb.Entry(master=container, textvariable=variable)
#         ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
#
#     def set_frame(self, name):
#         self.current_frame = name
#         self.frames[name].pack(side=LEFT, anchor=N)


app = App(theme="lumen")
app.place_window_center()
app.mainloop()
