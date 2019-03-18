
from prettytable import PrettyTable
from itemCategoryDao import ItemCategoryDao
from itemCategory import ItemCategory

class ItemCategories:

    def __init__(self, db):
        self.categoryDao = ItemCategoryDao(db)
        self.categorySection()

    def categorySection(self):
        print("Acciones a realizar: \n \
            1. Ingresar una nueva categoria\n \
            2. Actualizar una categoria\n \
            3. Eliminar una categoria\n \
            4. Ver todas las categorias")
        action = input("Ingrese el número de la acción que desea realizar: ")
        if action == "1":
            description = input("Descripción: ")
            new_category = ItemCategory(description)
            self.categoryDao.addCategory(new_category)
            self.printAllCategories()
        elif action == "2":
            self.printAllCategories()
            id_category = int(input("Ingrese el id de la categoria que desea cambiar: "))
            update = input("Ingrese la nueva descripción: ")
            self.categoryDao.updateCategory(id_category, update)
            self.printAllCategories()
        elif action == "3":
            self.printAllCategories()
            id_delete = int(input("Ingrese el id de la categoria a eliminar: "))
            self.categoryDao.deleteCategory(id_delete)
            self.printAllCategories()
        elif action == "4":
            self.printAllCategories()
        else:
            print("Ingrese un número válido")

    def printAllCategories(self):
        table = PrettyTable(["Id", "Descripción"])
        all_categories = self.categoryDao.getAllCategories()
        for category in all_categories:
            table.add_row(category)
        print(table)
