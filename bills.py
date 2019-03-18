from prettytable import PrettyTable
from bill import Bill
from billDao import BillDao

class Bills:

    def __init__(self, db):
        self.billDao = BillDao(db)
        self.billSection()

    def billSection(self):
        print("Acciones a realizar: \n \
            1. Ingresar una nueva factura\n \
            2. Actualizar una factura\n \
            3. Eliminar una factura\n \
            4. Ver todas las facturas")
        action = input("Ingrese el número de la acción que desea realizar: ")
        if action == "1":
            date = input("Fecha: ")
            client = input("Id del cliente: ")
            state = input("Estado: ")
            n_items = input("Número de items a ingresar: ")
            items = ""
            for item in range(int(n_items)):
                aux = input("Ingrese el id del item") + "-"
                items += aux
            new_bill = Bill(date, client, state, items)
            self.itemDao.addBill(new_bill)
            self.printAllBills()
        elif action == "2":
            self.printAllBills()
            id_bill = int(input("Ingrese el id dela factura que desea cambiar: "))
            column = int(input("Ingrese la columna a cambiar: 0 (Fecha), 1 (Cliente),\
                 2 (Valor), 3 (Estado), 4 (items): "))
            if column == "4":
                n_items = input("Número de items a ingresar: ")
                items = ""
                for item in range(int(n_items)):
                    aux = input("Ingrese el id del item") + "-"
                    items += aux
                update = items
            else:
                update = input("Valor por el cual lo desea modificar: ")
            self.billDao.updateBill(id_bill, column, update)
            self.printAllBills()
        elif action == "3":
            self.printAllBills()
            id_delete = int(input("Ingrese el id de la factura a eliminar: "))
            self.billDao.deleteBill(id_delete)
            self.printAllItems()
        elif action == "4":
            self.printAllItems()
        else:
            print("Ingrese un número válido")

    def printAllBills(self):
        table = PrettyTable(["Nro factura", "Fecha", "Id Cliente", "Valor", "Estado", "Id Items"])
        all_bills = self.billDao.getAllBills()
        for bill in all_bills:
            table.add_row(bill)
        print(table)