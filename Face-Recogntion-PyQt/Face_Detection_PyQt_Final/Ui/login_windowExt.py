from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
from login_window import Ui_MainWindow
import os
import sys

# Get base path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(current_dir)
sys.path.append(base_path)

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
                          Qt.WindowType.WindowCloseButtonHint)

        # Center the window on screen
        self.setWindowTitle("Admin Login")

    def login(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password")
            return

        # Import AdminAccount class for authentication
        from models.admin_accounts import AdminAccount

        # Use the static authenticate method instead of creating an instance
        is_valid = AdminAccount.authenticate(username, password)

        if is_valid:
            # Success - hide this window and show parent
            self.hide()
            if self.parent:
                # Signal to the parent window that login was successful
                if hasattr(self.parent, 'handle_successful_login'):
                    self.parent.handle_successful_login()
                else:
                    self.parent.show()  # Show parent window if no handle_successful_login method
            self.close()  # Close the login window
        else:
            # Failed
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
            self.lineEditPassword.clear()
            self.lineEditPassword.setFocus()

    def clear_fields(self):
        self.lineEditUsername.clear()
        self.lineEditPassword.clear()
        self.lineEditUsername.setFocus()