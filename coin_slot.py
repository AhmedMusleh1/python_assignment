from money_slot import MoneySlot


class CoinSlot(MoneySlot):
    def __init__(self, acceptedInput=None):
        super().__init__(acceptedInput)
        if acceptedInput is not None:
            self.acceptedInput = acceptedInput
        else:
            self.acceptedInput = [10, 20, 50, 100]

    def change_returning(self, amount, listOfProducts, row, col):
        for i in self.acceptedInput:
            if listOfProducts[row][col].price < i:
                return amount - listOfProducts[row][col].price
        print('invalid payment')
