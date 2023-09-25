from typing import final


class MoneySlot:
    currency: final = "USD"

    def __init__(self, acceptedInput):
        self.acceptedInput = acceptedInput

    def add_acceptedInput(self, name):
        if name not in self.acceptedInput:
            self.acceptedInput.append(name)

    def delete_acceptedInput(self, name):
        if name in self.acceptedInput:
            self.acceptedInput.remove(name)

    def print_all_acceptedInputs(self):
        for element in self.acceptedInput:
            print(element)
