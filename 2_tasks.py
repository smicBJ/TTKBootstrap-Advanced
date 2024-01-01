import requests as req
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
from helpers.K import *


class App(tb.Window):
    def __init__(self):
        super().__init__()
        self.title("App with Authentication")
        self.width = 854
        self.height = 640
        self.geometry(f"{self.width}x{self.height}")

        # Initialize application state
        self.logged_in: bool = False
        self.email: str = ""
        self.token: dict = {}
        self.base_url: str = "http://10.6.21.76:8000"

        # Create and initialize the screens
        self.login_screen = LoginScreen(self)
        self.dashboard_screen = DashboardScreen(self)

        # Show the login screen by default
        self.show_login_screen()

    def show_login_screen(self):
        self.login_screen.pack(expand=TRUE, fill=BOTH, pady=(0, PXL))
        self.dashboard_screen.pack_forget()

    def show_dashboard_screen(self):
        self.login_screen.pack_forget()
        self.dashboard_screen.pack(expand=TRUE, fill=BOTH)
        self.dashboard_screen.update_welcome_label()

    @staticmethod
    def handle_json_error(status_code, detail):
        toast = ToastNotification(
            title=f"{status_code} Error",
            message=detail,
            duration=3000,
        )
        toast.show_toast()

class LoginScreen(tb.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.container = tb.Frame(self)
        self.container.pack(padx=self.master.width / 4, expand=TRUE, fill=X)

        tb.Label(self.container, text="Login", font=H3).pack(pady=PM, fill=X)

        tb.Label(self.container, text="Email:").pack(pady=PXS, expand=TRUE, fill=BOTH)
        self.email_entry = tb.Entry(self.container)
        self.email_entry.pack(pady=PXS, fill=X)

        tb.Label(self.container, text="Password:").pack(pady=PXS, expand=TRUE, fill=BOTH)
        self.password_entry = tb.Entry(self.container, show="*")
        self.password_entry.pack(pady=PXS, fill=X)

        login_button = tb.Button(self.container, text="Login", command=self.login)
        login_button.pack(pady=PM, expand=TRUE, anchor=E)

    def login(self):
        form_data = {
            "username": self.email_entry.get(),
            "password": self.password_entry.get()
        }

        try:
            auth = req.post(f"{self.master.base_url}/token", data=form_data)
            status_code = auth.status_code
            data = auth.json()

            if status_code == 200:
                self.master.token = data
                self.master.logged_in = True
                self.master.email = form_data.get("username")
                self.password_entry.delete(0, tb.END)
                self.master.show_dashboard_screen()
            else:
                self.master.handle_json_error(status_code, data.get("detail"))
        except Exception as err:
            print(err)
            self.master.handle_json_error(401, "Bad Credentials")


class DashboardScreen(tb.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.header_container = tb.Frame(self, bootstyle=PRIMARY)
        self.header_container.pack(fill=X, ipady=PXS)

        self.body_container = tb.Frame(self)
        self.body_container.pack(expand=TRUE, fill=BOTH)

        self.welcome_label = tb.Label(self.header_container, text="", bootstyle=(INVERSE, PRIMARY))
        self.welcome_label.pack(side=LEFT, expand=TRUE, anchor=W, padx=PS)

        logout_button = tb.Button(
            self.header_container,
            text="Logout",
            command=self.logout,
            bootstyle=SECONDARY
        )
        logout_button.pack(side=LEFT, padx=PS)

    def update_welcome_label(self):
        self.welcome_label.config(text=self.master.email)

    def logout(self):
        self.master.logged_in = False
        self.master.show_login_screen()

if __name__ == "__main__":
    app = App()
    app.place_window_center()
    app.mainloop()
