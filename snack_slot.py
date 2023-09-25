from typing import final


class SnackSlot:
    rows: final = 5
    cols: final = 5

    def __init__(self, listOfProducts):
        if listOfProducts is not None:
            self.listOfProducts = listOfProducts
        else:
            self.listOfProducts = [[SnackSlot.cols] * SnackSlot.rows]

    def add_to_products(self, rowIndex, product):
        self.listOfProducts.insert(rowIndex, product)

    def print_all_products(self):
        for i in self.listOfProducts:
            for j in i:
                print("ID: " + str(j.id) + " | " + "Name: " + j.name + " | " + "Price:" + str(
                    j.price) + " | " + " is available?: " + str(j.isAvailable))
            print("")

    def product_buy_func(self, row, col):
        if self.listOfProducts[row][col].isAvailable:
            self.listOfProducts[row][col].remaining_quantity = self.listOfProducts[row][col].remaining_quantity - 1

            if self.listOfProducts[row][col].remaining_quantity < 1:
                self.listOfProducts[row][col].isAvailable = False
        else:
            print("this Product can't be bought")

    def print_products_names(self):
        row_counter = 0
        for i in self.listOfProducts:
            row_counter = row_counter + 1
            if row_counter >= len(self.listOfProducts):
                continue
            print(" Row: " + str(row_counter) + " >>> ", end=" ")
            for j in i:
                print(j.name + " | ", end=" ")
            print(" ")
