def tax_transaction(balance, money_to_pay):
    """
    Transaction function that deducts money from balance after applying tax.
    """
    def tax_decorator(func):
        def wrapper(balance, money_to_pay):
            if balance >= money_to_pay:
                money_to_pay_with_tax = money_to_pay + 1
                if balance >= money_to_pay_with_tax:
                    balance -= money_to_pay_with_tax
                    print(f"Transaction successful. Remaining balance: {balance}")
                else:
                    print("Insufficient funds after tax.")
            else:
                print("Insufficient funds.")
        return wrapper
    return tax_decorator


@tax_transaction(balance=100, money_to_pay=30)
def make_transaction(balance, money_to_pay):
    """
    Function to perform a transaction.
    """
    pass


make_transaction(100, 30)
make_transaction(50, 60)
make_transaction(10, 10)
