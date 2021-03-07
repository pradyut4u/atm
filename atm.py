class Atm:
    def __init__(self,cardno,pin):
        self.cardno=cardno
        self.pin=pin
        self.amount=5000
    def withdraw(self):
        a=int(input('How much do you want to withdraw'))
        if(a>self.amount):
            print('insuficient balance')
        else:
            self.amount=self.amount-a
            print(self.amount)

q=Atm(84822,54848)
q.withdraw()