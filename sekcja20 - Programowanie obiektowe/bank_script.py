from bank_account import BankAccount, MinimumBalanceAccount

konto = BankAccount(500)

amountToWithdraw = 300

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_to_withdraw(500)

if (result.is_ok()):
    print(result.message)
else:
    print(result.message, "poszło źle")
