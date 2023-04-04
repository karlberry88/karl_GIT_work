from account import Account

some_account = Account(1000.00)
some_account.deposit(550.23)
some_account.deposit(100)
some_account.withdraw(50)

print(some_account.getbalance())

another = Account(0)
another.deposit(10)

eoghan = Account(1000000000000)
eoghan.deposit(10000)

print(another.getbalance())
print(eoghan.getbalance())
print(Account.numCreated)

print("object another is class", another.__class__.__name__)
print(eoghan.__class__.__name__)
print(eoghan)
print(another)
# Overriding operators
if eoghan > another:
    print(f"{eoghan} has more money than {another}!")
if another < some_account:
    print(f"{another} has less money than {some_account}!")

# Using a class method
print(Account.get_total_balance())
