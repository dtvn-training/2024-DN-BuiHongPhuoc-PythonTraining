from datetime import datetime
from withdrawHistory import withdrawHistory 
from account import Account
from bank import Bank
now = datetime.now()

def main():
    bank = Bank()
    account = Account()
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
            result_check = bank.check_account(account_number)
            if (len(account_number) == 6 and (account_number.isdigit()) and result_check[0] != True ):
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
                print("vui long nhap 6 ki tu so hoac tai khoan da ton tai!")
        elif choice == "3":
            account_number = (input("Nhap ma so tai khoan gom 6 chu so: "))
            result_check = bank.check_account(account_number)
            if (len(account_number) == 6 and (account_number.isdigit()) and result_check[0] != True  ):
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
                print("vui long nhap 6 ki tu so hoac tai khoan da ton tai!")
        elif choice == "4":
            print(bank.customer_info)
            account_number = (input("Nhap ma gom 6 chu so tai khoan muon rut tien: "))
            result_check = bank.check_account(account_number)
            if result_check[0]:
                index = result_check[1]
                money = float(input("Nhap so tien muon rut: "))
                if bank.customer_info[index].typeAcc == 'Saving Account' :
                    account.fee = 0
                else: account.fee = 5000

                if (bank.customer_info[index].balance < (money + account.fee)):
                    print('so du khong du')
                else:
                    account.withdrawMoney = money
                    account.finalBalance = bank.customer_info[index].balance - money - account.fee
                    bank.customer_info[index].balance = account.finalBalance
                    account.withdrawHistoryList.append([account_number, account.dateTime,account.withdrawMoney,account.finalBalance,account.fee,account.atmBank])
                    bank.withdrawHistoryList.append(bank.customer_info[index].withdrawHistoryList)
                    print('Rut tien thanh cong')

        elif choice == "5":
            account_number = (input("Nhap ma gom 6 chu so tai khoan muon xem lich su: "))
            report = []

            for i,history in enumerate(account.withdrawHistoryList):
                if history[0] == account_number:
                    print('index',i)
                    report.append(history)
            
            print(report,'report')

            if len(report)>0:
                print('Lich su rut tien tai khoan: {}',account_number)
                for history in report:
                    print('---------------------------------------------------------')
                    print('- Ngay rut:  {}',history[1])
                    print('- So tien rut::  {}',history[2])
                    print('- So du con lai:  {}',history[3])
                    print('- Phi:  {}',history[4])
                    print('- ATM:  {}',history[5])
                    print('---------------------------------------------------------')

            else:
                print('Khong co lich su')

        elif choice == "0":
            print("Cam on da su dung dich vu cua chung toi.")
            break
        else:
            print("Lua chon khong hop le. Vui long thu lai.")

if __name__ == "__main__":
    main()
