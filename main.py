from datetime import datetime

now = datetime.now()


class withdrawHistory:
    def __init__(self, dateTime, withdrawMoney, finalBalance, fee, atmBank ):
        self.dateTime = dateTime
        self.withdrawMoney = withdrawMoney
        self.finalBalance = finalBalance
        self.fee  = fee
        self.atmBank = atmBank

class Account(withdrawHistory):
    def __init__(self, account_number='', typeCard='Standard', typeAcc='Saving Account', balance=0, dateTime=now, withdrawMoney=0, finalBalance=0, fee=0, atmBank='ATM-1'):
        super().__init__(dateTime, withdrawMoney, finalBalance, fee, atmBank ) 
        self.account_number = account_number
        self.typeAcc = typeAcc
        self.typeCard = typeCard
        self.balance  = balance
        self.withdrawHistoryList = []
    def getTypeCard(self, typeCard):
        if typeCard == '1':
            return 'Standard'
        elif typeCard =='2':
            return 'Premium'
        else: print('vui long chon lai loai the')

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
        for customer in self.customer_info:
            # print(customer.typeBank, customer.account_number, customer.typeAcc, customer.typeCard, customer.balance,customer.typeCus,'fghhat') check
            if customer.account_number == accountNumber:
                result = [True, 1]
                return result
            else:
                result = [False]
                return result
    
    # def withdraw(self, money, index):
    #     if self.customer[index-1].typeAcc == 'Saving Account' :
    #             self.fee = 0
    #         else: self.fee = '5000'
    #     if (self.customer_info[index-1].balance < (money + self.fee)):
    #         return print('so du khong du')
    #     else:
    #         self.withdrawMoney = self.customer[index].balance - money - self.fee
    #         self.customer[index-1].balance = self.withdrawMoney
            
    #         return print('Rut tien thanh cong')
        

    def display_history(self):
        for customer in self.customer_info:
            print(
            "Bank type: {} | Account Number: {} | Type of account: {} | Type of Card: {} | Balance: {} | Customer type: {} "
            .format(customer.typeBank, customer.account_number, customer.typeAcc, customer.typeCard, customer.balance,customer.typeCus)
            )

class Helper:
    def checkAccountNumber(account_number):
        if (len(account_number) == 6 and (account_number.isdigit())  ):
            return True
        else:
            return False 
    # def createAccount(self, numberInput):
    #     if numberInput == 2:
    #         account_number = (input("Nhap ma so tai khoan gom 6 chu so: "))
    #         if checkAccountNumber(account_number):
    #             typeAcc = 'Saving Account'
    #             balance = float(input("Nhap so du: "))          
    #             customer = Bank(account_number= account_number, balance=balance, typeAcc=typeAcc)
    #             bank.add_account(customer) 
    #             print("Tai khoan da duoc them.")
    #         else: 
    #             print("vui long nhap 6 ki tu so!")
    #     elif numberInput ==3:
    #         self.typeCard = 'Premium'


def main():
    bank = Bank()
    account = Account()
    print(bank.typeBank,'bankkk')
    while True:
        print("NGAN HANG SO | Phuoc@v1.0.0")
        print("1. Thong tin khach hang")
        print("2. Them tai khoan ATM")
        print("3. Them tai khoan tin dung")
        print("4. Rut tien")
        print("5. Lich su giao dich")
        print("0. Thoat")
        choice = input("Chon chuc nang: ")

        if choice == "1":
            bank.display_customer_info()
        elif choice == "2":
            account_number = (input("Nhap ma so tai khoan gom 6 chu so: "))
            if (len(account_number) == 6 and (account_number.isdigit())  ):
                print('xin moi chon loai the: \n')
                print('1: Standard \n')
                print('2: Premium \n')
                inputNumber = input('Lua chon:' )
                typeCard = bank.getTypeCard(inputNumber)
                balance = float(input("Nhap so du: "))
                customer = Bank(account_number = account_number, balance = balance, typeCard = typeCard)
                bank.add_account(customer) 
                 
                print("Tai khoan da duoc them.")
            else: 
                print("vui long nhap 6 ki tu so!")
        elif choice == "3":
            account_number = (input("Nhap ma so tai khoan gom 6 chu so: "))
            if (len(account_number) == 6 and (account_number.isdigit())  ):
                typeAccount = 'loan Account'
                print('xin moi chon loai the: \n')
                print('1: Standard \n')
                print('2: Premium \n')
                inputNumber = input('Lua chon:' )
                typeCard = bank.getTypeCard(inputNumber)
                balance = float(input("Nhap so du: "))          
                customer = Bank(account_number= account_number, balance=balance, typeAcc = typeAccount)
                bank.add_account(customer) 
                print("Tai khoan da duoc them.")
            else: 
                print("vui long nhap 6 ki tu so!")
        elif choice == "4":
            print(bank.customer_info)
            account_number = (input("Nhap ma gom 6 chu so tai khoan muon rut tien: "))
            result_check = bank.check_account(account_number)
            if result_check[0]:
                money = float(input("Nhap so tien muon rut: "))
                if bank.customer_info[result_check[1]-1].typeAcc == 'Saving Account' :
                    account.fee = 0
                else: account.fee = '5000'
                if (bank.customer_info[result_check[1]-1].balance < (money + account.fee)):
                    return print('so du khong du')
                else:
                    account.withdrawMoney = money
                    account.finalBalance = bank.customer_info[result_check[1]].balance - money - account.fee
                    bank.customer_info[result_check[1]-1].balance = account.finalBalance
                    account.append(bank.customer_info[result_check[1]-1].withdrawHistoryList)
                    return print('Rut tien thanh cong')  
            
        elif choice == "5":
            account_number = (input("Nhap ma gom 6 chu so tai khoan muon xem lich su: "))
            # if bank.check_account(account_number)[0]:
            # if bank.check_account(account_number)[0]:

            pass
        elif choice == "0":
            print("Cam on da su dung dich vu cua chung toi.")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")

if __name__ == "__main__":
    main()
