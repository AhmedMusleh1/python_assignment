from vending_machine import VendingMachine
from product import Product
from snack_slot import SnackSlot
from money_slot import MoneySlot


def main():
    SnackSlotObject = SnackSlot(listOfProducts=[[]])

    product_1 = Product(name="Kit kat", price=100)
    product_2 = Product(name="Bounty", price=80)
    product_3 = Product(name="Snickers", price=120)
    product_4 = Product(name="Mars", price=110)
    product_5 = Product(name="Kinder", price=90)

    SnackSlotObject.add_to_products(0, [product_1, product_2, product_3, product_4, product_5])

    product_1 = Product(name="mister chips", price=150)
    product_2 = Product(name="Doritos", price=150)
    product_3 = Product(name="Qasrawi", price=120)
    product_4 = Product(name="Lays", price=110)
    product_5 = Product(name="Cheetos", price=100)

    SnackSlotObject.add_to_products(1, [product_1, product_2, product_3, product_4, product_5])

    product_1 = Product(name="CocaCola", price=190)
    product_2 = Product(name="Pepsi", price=180)
    product_3 = Product(name="Mountain Dew", price=160)
    product_4 = Product(name="Fanta", price=150)
    product_5 = Product(name="7up", price=170)

    SnackSlotObject.add_to_products(2, [product_1, product_2, product_3, product_4, product_5])

    product_1 = Product(name="Bavaria", price=200)
    product_2 = Product(name="Fayroz", price=210)
    product_3 = Product(name="XL", price=190)
    product_4 = Product(name="power horse", price=180)
    product_5 = Product(name="Red Bull", price=190)

    SnackSlotObject.add_to_products(3, [product_1, product_2, product_3, product_4, product_5])

    product_1 = Product(name="Blu Day", price=150)
    product_2 = Product(name="Blu Mojito", price=150)
    product_3 = Product(name="Blu standard", price=150)
    product_4 = Product(name="Blu Blueberry", price=150)
    product_5 = Product(name="Blu Watermelon", price=150)

    SnackSlotObject.add_to_products(4, [product_1, product_2, product_3, product_4, product_5])

    VendingMachineObject = VendingMachine(SnackSlot=SnackSlotObject, MoneySlot=MoneySlot(acceptedInput=None))
    SnackSlotObject.print_products_names()

    # requested_row = 3
    # requested_col = 3
    # print(SnackSlotObject.listOfProducts[requested_row-1][requested_col-1].name)
    # VendingMachineObject.paymentMethod(row=requested_row, col=requested_col, amount=2000, listOfProducts=SnackSlotObject.listOfProducts)
    # VendingMachineObject.paymentMethod(row=2, col=2, amount=2000, listOfProducts=SnackSlotObject.listOfProducts)
    # VendingMachineObject.paymentMethod(row=1, col=1, amount=5000, listOfProducts=SnackSlotObject.listOfProducts)

    # print(SnackSlotObject.listOfProducts[0][0].remaining_quantity)

    # To Check the validity of the remaining quantity of the product
    # print(product_1.isAvailable)
    # print(product_1.remaining_quantity)
    # SnackSlotObject.product_buy_func(1, 1)
    # print(product_1.remaining_quantity)
    # SnackSlotObject.product_buy_func(1, 1)
    # SnackSlotObject.product_buy_func(1, 1)
    # SnackSlotObject.product_buy_func(1, 1)
    # print(product_1.remaining_quantity)
    # SnackSlotObject.product_buy_func(1, 1)
    # print(product_1.remaining_quantity)
    # print(product_1.isAvailable)
    # SnackSlotObject.product_buy_func(1, 1)


if __name__ == '__main__':
    main()
