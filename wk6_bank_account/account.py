class Account:
    numCreated = 0
    totalDeposits = 0

    def __init__(self, initial): # <-- 1000.00
        self._balance = initial  # _balance <-- 1000.00
        Account.numCreated += 1     # numCreated = 1
        Account.totalDeposits += initial
    def deposit(self, amt):
        self._balance += amt
        Account.totalDeposits += amt

    def withdraw(self,amt):
        self._balance -= amt
        Account.totalDeposits -= amt

    def getbalance(self):
        return self._balance

    def add_interest(self, interest):
        pass

    def __str__(self):
        return f"Account id: ${self.getbalance()}"

    def __gt__(self, other):
       return self._balance > other.getbalance()

    def __lt__(self, other):
       return self._balance < other.getbalance()

    @classmethod
    def get_total_balance(cls):
        return f"The Bank of Eoghan has reserves of:  ${cls.totalDeposits}"