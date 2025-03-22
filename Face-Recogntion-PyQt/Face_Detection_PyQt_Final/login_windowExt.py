from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
from login_window import Ui_MainWindow
from manage_windowExt import Ui_ManageDialog


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # Connect buttons to functions
        self.pushButtonLogin.clicked.connect(self.login)
        self.pushButtonClear.clicked.connect(self.clear_fields)

        # Set up Enter key to trigger login
        self.lineEditPassword.returnPressed.connect(self.login)

        # Set window flags to make it modal
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.CustomizeWindowHint |
                            Qt.WindowType.WindowTitleHint | Qt.WindowType.WindowCloseButtonHint)

        # Center the window on screen
        self.setWindowTitle("Admin Login")

    def login(self):
        """Handle login button click"""
        username = self.lineEditUsername.text().strip()
        password = self.lineEditPassword.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return

        # Import AdminAccount class for authentication
        from admin_accounts import AdminAccount

        if AdminAccount.authenticate(username, password):
            self.accept_login()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def clear_fields(self):
        """Clear the username and password fields"""
        self.lineEditUsername.clear()
        self.lineEditPassword.clear()
        self.lineEditUsername.setFocus()

    def accept_login(self):
        """Process successful login"""
        # Hide the login window
        self.hide()

        # Open the manage window
        if self.parent:
            # Signal to the parent (output window) that login was successful
            self.parent.handle_successful_login()

        # Close the login window
        self.close()