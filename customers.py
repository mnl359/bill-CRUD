
from prettytable import PrettyTable
from customerDao import CustomerDao
from customer import Customer
from DBconnection import DBconnection

class Customers:

    def __init__(self, db):
        self.customerDao = CustomerDao(db)
        self.customerSection()

    def customerSection(self):
        print("Acciones a realizar: \n \
            1. Ingresar un nuevo cliente\n \
            2. Actualizar un cliente\n \
            3. Eliminar un cliente\n \
            4. Ver todos los clientes")
        action = input("Ingrese el número de la acción que desea realizar: ")
        if action == "1":
            name = input("Nombre: ")
            lastname = input("Apellido: ")
            gender = input("Género: ")
            birthday = input("Fecha de nacimiento: ")
            civil = input("Estado civil: ")
            new_customer = Customer(name, lastname, gender, birthday, civil)
            self.customerDao.addCustomer(new_customer)
            self.printAllCustomers()
        elif action == "2":
            self.printAllCustomers()
            id_customer = int(input("Ingrese el id del usuario que desea cambiar: "))
            column = int(input("Ingrese la columna a cambiar: 0 (Nombre), 1 (Apellido),\
                 2 (Género), 3 (Fecha de nacimiento), 4 (Estado civil): "))
            update = input("Valor por el cual lo desea modificar: ")
            self.customerDao.updateCustomer(id_customer, column, update)
            self.printAllCustomers()
        elif action == "3":
            self.printAllCustomers()
            id_delete = int(input("Ingrese el id del usuario a eliminar: "))
            self.customerDao.deleteCustomer(id_delete)
            self.printAllCustomers()
        elif action == "4":
            self.printAllCustomers()
        else:
            print("Ingrese un número válido")

    def printAllCustomers(self):
        table = PrettyTable(["Id", "Nombre", "Apellido", "Género", "Fecha de nacimiento", "Estado civil"])
        all_customers = self.customerDao.getAllCustomers()
        for customer in all_customers:
            table.add_row(customer)
        print(table)
