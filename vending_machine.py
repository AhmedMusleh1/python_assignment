from coin_slot import CoinSlot
from notes_slot import NotesSlot


def payment(amount, listOfProducts, row, col):
    if amount <= 100:
        obj = CoinSlot(acceptedInput=None)
        print(obj.change_returning(amount, listOfProducts, row, col))
    else:
        obj = NotesSlot(acceptedInput=None)
        print(obj.change_returning(amount, listOfProducts, row, col))


class VendingMachine:
    def __init__(self, SnackSlot, MoneySlot):
        self.SnackSlot = SnackSlot
        self.MoneySlot = MoneySlot

    def paymentMethod(self, row, col, amount, listOfProducts):
        payment(amount, listOfProducts, row - 1, col - 1)
        self.SnackSlot.product_buy_func(row - 1, col - 1)
