import pyperclip
import random
import string

class User:
    """
    Creates a user class that generates new intances of the User.
    """

    userList = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLoggedin = False
    def createUser(username, password):
        """
        Method that is used to create new user account
        """
        newUser = User(username, password)
        return newUser

    def login(self):
        """
        method that allows a user to log in after providing credentials
        """
        print("You have Successfully Logged in!!")

    def saveUser(self):
        """
        Method that saves a user to the list
        """
        User.userList.append(self)

    @classmethod
    def displayUser(cls):
        """
        method that displays saved users
        """
        return cls.userList

    def deleteUser(self):
        """
        method that delete a selected user
        """
        User.userList.remove(self)

if __name__ == "__main__":
    pass

class Credentials():
    """
    Method to create new user credentials
    """
    credentials = []

    def __init__(self, account, username, password):
        """
        crede
        """
        self.account = account
        self.username = username
        self.password = password

    def saveCredential(self):
        """
        method that adds credentials to the list
        """
        Credentials.credentials.append(self)

    @classmethod
    def createCredential(self, account, username, password):
        """
        method that creates a new credential
        """
        newCredential = Credentials(
            account, username, password)
        return newCredential

    def searchCredential(account):
        """
        Method that searches for credentials
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.account == account:
                    return credential
            print(" There is no account with those credentials")

        else:
            print("Credentials have not been saved")

    def displayCredential():
        """
        Method that displays saved credentials
        """
        if (len(Credentials.credentials) > 0):

            return Credentials.credentials

    @classmethod
    def credentialExist(self, account):
        """
        Method that checks if credentials exists
        """

        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.account == account:
                    return True
            print("Account doesn't exist")

        else:
            print("Credentials Not saved")

    def deleteCredential(account):
        """
        Method that deletes credential
        """
        for credential in Credentials.credentials:
            if credential.username == account:
                Credentials.credentials.remove(credential)

    def passwordGenerate(stringLength=8):
        """
        Method that generate a random password
        """
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))

if __name__ == "__main__":
    
    isTrue = True
    print("What is your name?")
    name= input()
    print(f"Hello {name} Welcome to password manager.An application that manages and generate passwords.")
    while isTrue == True:
        print(
            "Use these short codes to proceed:\n\n 1. ca-Create Account\n 2. ha-Have an existing Account\n")
        shortCode = input().lower()

        if shortCode == 'ca':
            print("Create New Account")
            print("*"*50)
            print("Username")
            username = input()

            while True:
                print(
                    "1. tp - Type your own password\n 2. gp - generate password from system")
                password = input()

                if password == 'tp':
                    print("Enter your Password:")
                    password = input()
                    break
                elif password == 'gp':
                    password = Credentials.passwordGenerate()
                    break

                else:
                    print("password is Invalid")

            createUser = User.createUser(username, password)
            User.saveUser(createUser)
            print("\n")
            print(
                f"Hi {username} Your account has been created sucessfully !\n")
            print(f"Your username is: {username} \n Your password is: {password}\n")

        elif shortCode == 'ha':
            print("*"*100)
            print("Enter your username and password")
            print("*"*100)

            print("Enter Username:")
            username = input()
            print("Enter Password:")
            password = input()

            for user in User.userList:
                if username == user.username:
                    if user.password == password:
                        print(user.login())
                    else:
                        print("password enterd is invalid")
                        break
                else:
                    print("username enetered is  Invalid")
                    break

            break
    while True:
        print("If you would like to proceed use the shortcodes below\n 1. sc - Save Credential \n 2. dc - Display Existing Credential\n 3. fc - Find credential \n 4. del -  Delete an existing Credential \n 5. ex - Exit")

        shortCode = input().lower()

        if shortCode == 'sc':
            print("Enter Your New Credential Account:")
            print("*"*100)
            print("\n")

            print("Enter Account Name e.g Instagram:")
            account = input()

            print("Enter Account UserName:")
            username = input()

            while True:
                print(
                    "1. tp - type your own password?\n 2. gp -generate password from system")

                password = input().lower()

                if password == 'tp':
                    print("Type Account Password :")
                    password = input()
                    break
                elif password == 'gp':
                    password = Credentials.passwordGenerate()
                    break

                else:
                    print("Password Entered is Invalid")

            newCredential = Credentials.createCredential(
                account, username, password)
            Credentials.saveCredential(newCredential)
            print("\n")
            print("Your Account Credentials have been saved!")
            print("\n")

        elif shortCode == 'dc':
            if Credentials.displayCredential():
                print(" Here is a List of your credentials:\n")
                for credential in Credentials.credentials:
                    account = credential.account
                    accountuser = credential.username
                    accountpassword = credential.password
                    print(
                        f"Account Name : {account}\n Account Username : {accountuser}\n Account Password: {accountpassword}\n")

            else:
                print("You do not have any saved credentials\n")

        elif shortCode == 'fc':
            print("Enter Account name: ")
            Account = input()
            if Credentials.credentialExist(Account):
                searchAccount = Credentials.searchCredential(Account)
                print(
                    f"Account name: {searchAccount.account}\n Account Username: {searchAccount.username}\n Account Password : {searchAccount.password}")

            else:
                print("account name doesn't exist!\n")

        elif shortCode == 'del':
            print("Enter account that you would like to delete this account?")
            Account = input()
            if Credentials.credentialExist(Account):
                Credentials.deleteCredential(Account)
                print("Account has been Successfully deleted")

            else:
                print("account name doesn't exist")

        elif shortCode == 'ex':
            print("Thank you for using this application.")
            break

        else:
            print("invalid code")    
        
        

  
