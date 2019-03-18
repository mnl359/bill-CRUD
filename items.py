
from prettytable import PrettyTable
from itemDao import ItemDao
from item import Item

class Items:

    def __init__(self, db):
        self.itemDao = ItemDao(db)
        self.itemSection()

    def itemSection(self):
        print("Acciones a realizar: \n \
            1. Ingresar un nuevo item\n \
            2. Actualizar un item\n \
            3. Eliminar un item\n \
            4. Ver todos los items")
        action = input("Ingrese el número de la acción que desea realizar: ")
        if action == "1":
            item_type = int(input("Tipo de item: "))
            description = input("Descripción: ")
            value = int(input("Valor: "))
            new_item = Item(item_type, description, value)
            self.itemDao.addItem(new_item)
            self.printAllItems()
        elif action == "2":
            self.printAllItems()
            id_item = int(input("Ingrese el id del item que desea cambiar: "))
            column = int(input("Ingrese la columna a cambiar: 0 (Tipo), 1 (Descripción),\
                 2 (Value): "))
            update = input("Valor por el cual lo desea modificar: ")
            self.itemDao.updateItem(id_item, column, update)
            self.printAllItems()
        elif action == "3":
            self.printAllItems()
            id_delete = int(input("Ingrese el id del item a eliminar: "))
            self.itemDao.deleteItem(id_delete)
            self.printAllItems()
        elif action == "4":
            self.printAllItems()
        else:
            print("Ingrese un número válido")

    def printAllItems(self):
        table = PrettyTable(["Id", "Id Tipo", "Descripción", "Valor"])
        all_items = self.itemDao.getAllItems()
        for item in all_items:
            table.add_row(item)
        print(table)
