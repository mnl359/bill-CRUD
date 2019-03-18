
class CustomerDao:

    def __init__(self, db):
        self.db = db

    def getAllCustomers(self):
        get_customers = "SELECT * FROM customers;"
        cursor = self.db.execute(get_customers)
        all_customers = []
        for customer in cursor:
            all_customers.append(customer)
        return all_customers

    def updateCustomer(self, customer_id, column, update):
        col = ""
        if column == 0:
            col = "name"
        elif column == 1:
            col = "lastname"
        elif column == 2:
            col = "gender"
        elif column == 3:
            col = "birthday"
        else:
            col = "civil"
        update_customer = "UPDATE customers SET %s = '%s' WHERE id = %d"\
                            % (col, update, customer_id)
        self.db.execute(update_customer)
        self.db.commit()

    def deleteCustomer(self, customer_id):
        delete_customer = "DELETE FROM customers WHERE id = %d ;" % (customer_id)
        self.db.execute(delete_customer)
        self.db.commit()

    def addCustomer(self, customer):
        table_not_exist = "CREATE TABLE IF NOT EXISTS customers("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "name TEXT NOT NULL, lastname TEXT NOT NULL,"\
                            "gender TEXT NOT NULL, birthday TEXT NOT NULL,"\
                            "civil TEXT NOT NULL);"
        self.db.execute(table_not_exist)
        self.db.commit()
        cursor = self.db.execute("SELECT id FROM customers ORDER BY id \
                                DESC LIMIT 1;")
        last_id = None
        for row in cursor:
            last_id = int(row[0])
            break
        if last_id != None:
            customer_id = last_id + 1
        else:
            customer_id =  0
        self.db.execute("INSERT INTO customers (id, name, lastname, gender, \
                        birthday, civil) VALUES (?,?,?,?,?,?);" , (customer_id,
                        customer.name, customer.lastname, customer.gender, customer.birthday,
                        customer.civil))
        self.db.commit()
