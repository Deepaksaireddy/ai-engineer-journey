import hashlib

class Login:
    def __init__(self):
        self.user_type = None
        self.Username = ""
        self.Password = ""
        self.users = {
            "MEMBER":{
                "Username" :"MEMBER",
                "Password" : self.hash_password("user@123")},
            "LIBUSER":{
                "Username" : "LIBUSER",
                "Password" : self.hash_password("admin@123")
            }
        }

    def hash_password(self,passcode):
        return hashlib.sha256(passcode.encode()).hexdigest()

    def display_menu(self):
        print("--------------------------------------")
        print(" Welcome to Library Management System")
        print("--------------------------------------")
        print("1. Member")
        print("2. Librarian")

    def Login(self):
        self.display_menu()
        try:
            option = int(input("Please select a user type"))
            if option == 1:
                self.user_type = "MEMBER"
            elif option == 2:
                self.user_type = "LIBUSER"
            else:
                print("Invalid User option selected")
                return False

        except ValueError:
            print("Please enter numbers only")
            return False

        self.Username = input("Username: ").upper()
        self.Password = input("Password: ")

        hashed_password = self.hash_password(self.Password)

        db_user = self.users[self.user_type]

        if self.Username == db_user["Username"] and hashed_password == db_user["Password"]:
            print(f"\nWelcome, {self.Username}!")
            return True
        print("\nInvalid username or password.")
        return False