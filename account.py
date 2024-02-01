from datetime import datetime
from withdrawHistory import withdrawHistory 

now = datetime.now()
class Account(withdrawHistory):
    def __init__(self, account_number='', typeCard='Standard', typeAcc='Saving Account', balance=0, dateTime=now, withdrawMoney=0, finalBalance=0, fee=0, atmBank='ATM-1', withdrawHistoryList = None):
        super().__init__(dateTime, withdrawMoney, finalBalance, fee, atmBank )
        self.account_number = account_number
        self.typeAcc = typeAcc
        self.typeCard = typeCard
        self.balance  = balance
        self.withdrawHistoryList = withdrawHistoryList if withdrawHistoryList is not None else []
    def getTypeCard(self, typeCard):
        if typeCard == '1':
            return 'Standard'
        elif typeCard =='2':
            return 'Premium'
        else: print('vui long chon lai loai the')
    def check_history(self, accountNumber):
        result = []
        print(self.withdrawHistoryList)
        for i,history in enumerate(self.withdrawHistoryList):
            if history[i][0] == accountNumber:
                result.append(i)
        if len(result)>0:
            return [True,result]
        else:
            result = [False]
            return result