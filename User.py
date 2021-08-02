import unittest
from user import User
from user import Credentials
import pyperclip

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the Users class behaviours.
    """
    def setUp(self):
        '''
        method to run each test
        '''
        self.user = User("kitili", "shena2308")

    def test_init(self):
        '''
        Test to check proper user initialization
        '''
        self.assertEqual(self.user.username, "kitili")
        self.assertEqual(self.user.password, "shena2308")

    def test_save_multiple_users(self):
        '''
        method to test multiple saved users
        '''
        self.user.saveUser()
        test_user = User("katana", "katana") 
        test_user.saveUser()

        self.assertEqual(len(User.userList), 2)

    def tearDown(self):
        '''
        method to clean up after each test
        '''

        User.userList = []

    
    def test_delete_user(self):
        """
        method to test delete users
        """
        self.user.saveUser()
        test_user = User("katana", "katana") 
        test_user.saveUser()

        self.user.deleteUser()
        self.assertEqual(len(User.userList), 1)

    def test_display_users(self):
        """
        method to test if users are correctly displayed
        """
        self.assertEqual(User.displayUser(), User.userList)

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Method to define the constructor
        """
        self.cred = Credentials("Instagram", "@love_kiki", "tlo")

    def test_init(self):
        """
        make sure the credential is well initialized
        """
        self.assertEqual(self.cred.account, "Instagram")
        self.assertEqual(self.cred.username, "@love_kiki")
        self.assertEqual(self.cred.password, "tlo")

    def tearDown(list):
        """
        clear up during each test
        """
        Credentials.credentials = []

    def test_save_multiples_credential(self):
        """
        test for multiple credentials
        """
        self.cred.saveCredential()
        test_cred = Credentials("Instagram", "@love_kiki", "tlo") 
        test_cred.saveCredential()

        self.assertEqual(len(Credentials.credentials), 2)

    def test_delete(self):
        """
        test to delete credentials
        
        """
        self.cred.saveCredential()
        test_cred = Credentials("Instagram", "@love_kiki", "tlo") 
        test_cred.saveCredential()

        self.cred.deleteCredential()
        self.assertEqual(len(Credentials.credentials), 2)

  

if __name__ == "__main__":
    unittest.main()    
