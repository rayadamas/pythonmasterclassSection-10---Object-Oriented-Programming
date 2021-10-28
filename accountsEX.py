import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1 # to show us a negative number
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    BLV = Account("BLV", 0)
    BLV.show_balance()

    BLV.deposit(1000)
    # BLV.show_balance()
    BLV.withdraw(500)
    # BLV.show_balance()

    BLV.withdraw(2000)

    BLV.show_transactions()

    vanessa = Account("Vanessa", 800)
    vanessa.__balance = 200
    vanessa.deposit(100)
    vanessa.withdraw(200)
    vanessa.show_transactions()
    vanessa.show_balance()
    print(vanessa.__dict__)
