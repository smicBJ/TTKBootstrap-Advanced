import ttkbootstrap as tb
from ttkbootstrap.constants import *


app = tb.Window()
app.title("TTKBootstrap Intro")
app.geometry("1280x720")

first_label = tb.Label(app, text="Hello World!", font=("Roboto", 40, "bold"), bootstyle=(INVERSE, PRIMARY))
first_label.pack(ipadx=20, ipady=20, pady=(0, 20))

second_label = tb.Label(app, text="Second Label", font=("Roboto", 40, "bold"), bootstyle=(INVERSE, DANGER))
second_label.pack(ipadx=20, ipady=20)

app.place_window_center()
app.mainloop()
