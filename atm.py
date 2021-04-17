class atm(object):
    def __init__(self,atmCardNumber,AtmPinNumber):
        self.atmCardNumber=atmCardNumber
        self.AtmPinNumber=AtmPinNumber


    def CashWithdraw(self):
        cash=input('WRITE THE AMOUNT : ')
        print(cash, "Withdraw successfully")

    def balanceInquiry(self):
        if self.atmCardNumber==111111111:
            print("Available balance is 1000000")
        else:
            print("Account is not available")        

ff=atm(111111111,1234)
print("Card Number :", ff.atmCardNumber)
print("Atm Pin : ", ff.AtmPinNumber)
ff.CashWithdraw()
ff.balanceInquiry()