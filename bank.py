from datetime import datetime
from withdrawHistory import withdrawHistory 
from account import Account
now = datetime.now()

class Bank(Account):
    def __init__(
            self,
            account_number='', balance=0, typeCard ='Standard', typeAcc = 'Saving Account', dateTime=now, withdrawMoney=0, finalBalance=0, fee=0, atmBank='ATM-1', withdrawHistoryList=[''],
            typeCus='Digital Customer', typeBank='DigitalBank'):
        super().__init__(account_number, typeCard, typeAcc, balance, dateTime, withdrawMoney, finalBalance, fee, atmBank )
        self.customer_info = []
        self.typeCus = typeCus
        self.typeBank = typeBank

    def getTypeCard(self, typeCard):
        return super().getTypeCard(typeCard)

    def add_account(self, customer):
        self.customer_info.append(customer)

    def display_customer_info(self):
        for customer in self.customer_info:
            print(
            "Bank type: {} | Account Number: {} | Type of account: {} | Type of Card: {} | Balance: {} | Customer type: {} "
            .format(customer.typeBank, customer.account_number, customer.typeAcc, customer.typeCard, customer.balance,customer.typeCus)
            )
    def check_account(self, accountNumber):
        result = []
        for index,customer in enumerate(self.customer_info):
            if customer.account_number == accountNumber:
                result = [True, index]
        if len(result)==2:  
            return result
        else:
            result = [False]
            return result

    def display_history(self):
        for customer in self.customer_info:
            print(
            "Bank type: {} | Account Number: {} | Type of account: {} | Type of Card: {} | Balance: {} | Customer type: {} "
            .format(customer.typeBank, customer.account_number, customer.typeAcc, customer.typeCard, customer.balance,customer.typeCus)
            )