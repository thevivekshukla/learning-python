class Account:

  def __init__(self, filepath):
    self.filepath = filepath
    with open(filepath, 'r') as file:
      self.balance = int(file.read())


  def withdraw(self, amount):
    self.balance = self.balance - amount

  def deposit(self, amount):
    self.balance = self.balance + amount

  def commit(self):
    with open(self.filepath, 'w') as file:
      file.write(str(self.balance))


# account = Account("balance.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.withdraw(500)
# account.deposit(1000)
# print(account.balance)
# account.commit()


class Checking(Account):

  def __init__(self, filepath, fee):
    Account.__init__(self, filepath)
    self.fee = fee


  def transfer(self, amount):
    self.balance = self.balance - amount - self.fee


check = Checking('balance.txt', 5)
check.withdraw(600)
print(check.balance)
check.transfer(2000)
print(check.balance)
check.commit()
