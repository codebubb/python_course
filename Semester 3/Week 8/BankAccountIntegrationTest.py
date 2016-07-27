import unittest
from BankAccount import BankAccount

class TestBankAccountIntegration(unittest.TestCase):

    def setUp(self):
        # Create a new BankAccount object for the integration test
        self.BankAccount = BankAccount()

    def tearDown(self):
        # Clean up the object when finished
        self.BankAccount = None

    def test_depositing(self):
        # Check depositing method updates balance and transactions
        self.assertEqual(self.BankAccount.getBalance(), 0)
        self.assertEqual(len(self.BankAccount.transactions), 0)
        self.BankAccount.deposit(500)
        self.assertEqual(self.BankAccount.getBalance(), 500)
        self.assertEqual(len(self.BankAccount.transactions), 1)
        self.BankAccount.deposit(50)
        self.assertEqual(self.BankAccount.getBalance(), 550)
        self.assertEqual(len(self.BankAccount.transactions), 2)
    #
    # def test_withdrawing(self):
    #     # Check withdrawal method updates balance (only if available) and transactions
    #     self.assertEqual(self.BankAccount.getBalance(), 0)
    #     self.assertEqual(len(self.BankAccount.transactions), 0)
    #
    #     self.assertFalse(self.BankAccount.withdraw(500)) # Withdraw should return false as there is insufficient balance
    #     self.assertEqual(self.BankAccount.getBalance(), 0)
    #     self.assertEqual(len(self.BankAccount.transactions), 0)
    #
    #     self.BankAccount.deposit(500) # Deposit some money so withdrawal is possible
    #     self.assertEqual(self.BankAccount.getBalance(), 500)
    #     self.assertEqual(len(self.BankAccount.transactions), 1)
    #
    #     self.assertTrue(self.BankAccount.withdraw(500)) # Should now be possible as money has been deposited
    #     self.assertEqual(self.BankAccount.getBalance(), 0)
    #     self.assertEqual(len(self.BankAccount.transactions), 2)
    #

if __name__ == '__main__':
    unittest.main()
