from sys import exit

from DBconnection import DBconnection
from customers import Customers
from itemCategories import ItemCategories
from items import Items

def main():

    DBconnection()
    db = DBconnection.getInstance().connection

    while True:
        print("Acciones a realizar: \n \
                1. Cliente\n \
                2. Categorías de item\n \
                3. Items\n \
                4. Factura\n \
                5. Salir")
        action = input("Ingrese el número de la acción que desea realizar: ")
        if action == "1":
            customer = Customers(db)
        elif action == "2":
            category = ItemCategories(db)
        elif action == "3":
            item = Items(db)
        elif action == "4":
            pass
        elif action == "5":
            exit()
        else:
            print("Ingrese un número válido")

if __name__ == '__main__':
    main()

