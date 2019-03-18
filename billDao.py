
class BillDao:

    def __init__(self, db):
        self.db = db

    def getAllBills(self):
        get_bills = "SELECT * FROM bills;"
        cursor = self.db.execute(get_bills)
        all_bills = []
        for bill in cursor:
            all_bills.append(bill)
        return all_bills

    def updateBill(self, bill_id, column, update):
        item_update = 0
        if column == "0":
            col = "date"
        elif column == "1":
            col = "client"
            update = int(update)
        elif column == "2":
            col = "value"
            update = int(update)
        elif column == "3":
            col = "state"
        elif column == "4":
            col = "items"
            item_update = 1
        update_bill = "UPDATE bills SET %s = '%s' WHERE id = %d"\
                            % (col, update, bill_id)
        if item_update == 1:
            bill_value = 0
            items = update.split(" ")
            for item in items:
                exec_item = "SELECT value FROM items WHERE id = %s" % (item)
                item_cursor = self.db.execute(exec_item)
                for item_row in item_cursor:
                    bill_value += int(item_row[0])
                    break
            update_value = ("UPDATE bills SET value = '%d' WHERE id = %d"\
                            % (bill_value, bill_id))
        self.db.execute(update_bill)
        self.db.commit()

    def deleteBill(self, bill_id):
        delete_bill = "DELETE FROM bills WHERE id = %d ;" % (bill_id)
        self.db.execute(delete_bill)
        self.db.commit()

    def addBill(self, bill):
        self.db.execute("PRAGMA foreign_keys = ON;")
        table_not_exist = "CREATE TABLE IF NOT EXISTS bills("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "date TEXT NOT NULL, client int NOT NULL,"\
                            "value int NOT NULL, state TEXT NOT NULL,"\
                            "items text NOT NULL,"\
                            "FOREIGN KEY (client) REFERENCES customers(id));"
        self.db.execute(table_not_exist)
        self.db.commit()
        cursor = self.db.execute("SELECT id FROM bills ORDER BY id \
                                DESC LIMIT 1;")
        last_id = None
        for row in cursor:
            last_id = int(row[0])
            break
        if last_id != None:
            bill_id = last_id + 1
        else:
            bill_id =  0
        bill_value = 0
        items = bill.items.split("-")
        for item in items:
            exec_item = "SELECT value FROM items WHERE id = %s" % (item)
            item_cursor = self.db.execute(exec_item)
            for item_row in item_cursor:
                bill_value += int(item_row[0])
                break
        self.db.execute("INSERT INTO bills (id, date, client, value,\
                         state, items) VALUES (?,?,?,?,?,?);" , (bill_id,
                             bill.date, bill.client, bill_value, bill.state,
                             bill.items))
        self.db.commit()
