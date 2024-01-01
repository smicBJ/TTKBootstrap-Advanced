import ttkbootstrap as tb
from helpers.K import *

class Student:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

STUDENTS = [
    Student(name="Nolan", age=16, grade=11),
    Student(name="Hudson", age=16, grade=11),
    Student(name="Samuel", age=16, grade=11)
]


class SearchBarComp(tb.Frame):
    def __init__(self, master, y_spacing=PM):
        super().__init__(master)
        self.pack(pady=y_spacing, padx=PL, fill=X)

        self.entry = tb.Entry(self)
        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS, command=self.submit_action)

        self.entry.pack(side=LEFT, expand=TRUE, fill=X)
        self.submit_button.pack(side=LEFT, padx=(PM, 0))

    def submit_action(self):
        query = self.entry.get()
        response = None

        for student in STUDENTS:
            if student.name.lower() == query.lower():
                response = student

        if response is not None:
            self.master.results.configure(font=H1)
            response_text = f"NAME: {response.name}\nAGE: {response.age}\nGRADE: {response.grade}"
            self.master.results_text.set(response_text)
        else:
            self.master.results.configure(font=H3)
            self.master.results_text.set("No Student found with that query")



class ButtonGroupComp(tb.Frame):
    def __init__(self, master, y_spacing=PL):
        super().__init__(master)
        self.pack(pady=y_spacing, padx=PL, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.clear_button = tb.Button(self, text="Clear", bootstyle=WARNING)

        self.submit_button.pack(side=RIGHT, padx=(PS, 0))
        self.clear_button.pack(side=RIGHT)


class App(tb.Window):
    def __init__(self, theme):
        super().__init__(themename=theme)

        self.title("Frames")
        self.geometry("1280x720")

        self.results_text = tb.StringVar(value="No Results")

        self.title_label = tb.Label(self, text="Student Directory System", font=DISPLAY3, bootstyle=PRIMARY)
        self.subtitle_label = tb.Label(
            self,
            text="Use this to search up a student's information",
            font=H5,
            bootstyle=SECONDARY)
        self.results = tb.Label(self, textvariable=self.results_text, font=BODY, bootstyle=INFO)

        self.title_label.pack(pady=(PL, 0), padx=PL, fill=X)
        self.subtitle_label.pack(pady=(0, PM), padx=PL, fill=X)
        self.search_bar = SearchBarComp(self)
        self.results.pack(pady=PM, padx=PL, expand=TRUE)
        # self.button_group = ButtonGroupComp(self)


if __name__ == '__main__':
    app = App(theme="sandstone")
    app.place_window_center()
    app.mainloop()