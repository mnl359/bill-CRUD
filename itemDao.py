
class ItemDao:

    def __init__(self, db):
        self.db = db

    def getAllItems(self):
        get_items = "SELECT * FROM items;"
        cursor = self.db.execute(get_items)
        all_items = []
        for item in cursor:
            all_items.append(item)
        return all_items

    def updateItem(self, item_id, column, update):
        if column == "0":
            col = "type"
            update = int(update)
        elif column == "1":
            col = "description"
        elif column == "2":
            col = "value"
            update = int(update)
        update_item = "UPDATE items SET %s = '%s' WHERE id = %d"\
                            % (col, update, item_id)
        self.db.execute(update_item)
        self.db.commit()

    def deleteItem(self, item_id):
        delete_item = "DELETE FROM items WHERE id = %d ;" % (item_id)
        self.db.execute(delete_item)
        self.db.commit()

    def addItem(self, item):
        self.db.execute("PRAGMA foreign_keys = ON;")
        table_not_exist = "CREATE TABLE IF NOT EXISTS items("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "type int TEXT NOT NULL,"\
                            "description TEXT NOT NULL, value int NOT NULL,"\
                            "FOREIGN KEY (type) REFERENCES categories(id));"
        self.db.execute(table_not_exist)
        self.db.commit()
        cursor = self.db.execute("SELECT id FROM items ORDER BY id \
                                DESC LIMIT 1;")
        last_id = None
        for row in cursor:
            last_id = int(row[0])
            break
        if last_id != None:
            item_id = last_id + 1
        else:
            item_id =  0
        self.db.execute("INSERT INTO items (id, type, description,\
                         value) VALUES (?,?,?,?);" , (item_id,
                             item.item_type, item.description,
                             item.value))
        self.db.commit()
