from .controller import pin, account
class App:

    def __init__(self, pin_rule):
        self.pin_rule = pin.set_regexp(pin_rule)

    def login(self, pin):
        pin.check_pin(self.pin_rule,pin)
        return account.get_accounts(pin)
    
    def check_balance(account_id, pin): # 잔액조회
        return account.check_balance(account_id, pin)

    def withdraw(id,pin,dollar): #출금
        return account.withdraw(id,pin,dollar)
    
    def deposit(id,pin,dollar): # 입금
        return account.deposit(id,pin,dollar)
