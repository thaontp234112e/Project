import os

class AdminAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(self, input_password):
        """Verify if the input password matches the account password"""
        return self.password == input_password

    @staticmethod
    def get_base_path():
        """Get the base path of the application"""
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.dirname(current_dir)

    @staticmethod
    def load_accounts_from_csv(csv_path=None):
        """Load all admin accounts from CSV file"""
        import csv
        import os

        if csv_path is None:
            base_path = AdminAccount.get_base_path()
            csv_path = os.path.join(base_path, 'dataset', 'admin_accounts.csv')

        accounts = []

        if not os.path.exists(csv_path):
            # Create default admin account if file doesn't exist
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'password'])
                writer.writerow(['admin', 'admin123'])

        try:
            with open(csv_path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                for row in reader:
                    if len(row) >= 2:
                        accounts.append(AdminAccount(row[0], row[1]))
        except Exception as e:
            print(f"Error loading admin accounts: {e}")

        return accounts

    @staticmethod
    def authenticate(username, password, csv_path=None):
        """Authenticate an admin user"""
        if csv_path is None:
            base_path = AdminAccount.get_base_path()
            csv_path = os.path.join(base_path, 'dataset', 'admin_accounts.csv')
            
        accounts = AdminAccount.load_accounts_from_csv(csv_path)

        for account in accounts:
            if account.username == username and account.verify_password(password):
                return True

        return False