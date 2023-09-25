from money_slot import MoneySlot


class NotesSlot(MoneySlot):
    def __init__(self, acceptedInput=None):
        super().__init__(acceptedInput)
        if acceptedInput is not None:
            self.acceptedInput = acceptedInput
        else:
            self.acceptedInput = [2000, 5000]

    def change_returning(self, amount, listOfProducts, row, col):
        for i in self.acceptedInput:
            if listOfProducts[row][col].price < i:
                return amount - listOfProducts[row][col].price

        return "your Product is more than 50 Dollars"
