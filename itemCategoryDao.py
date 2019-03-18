
class ItemCategoryDao:

    def __init__(self, db):
        self.db = db

    def getAllCategories(self):
        get_categories = "SELECT * FROM categories;"
        cursor = self.db.execute(get_categories)
        all_categories = []
        for category in cursor:
            all_categories.append(category)
        return all_categories

    def updateCategory(self, category_id, update):
        update_category = "UPDATE categories SET description = '%s' WHERE id = %d ;"\
                            % (update, category_id)
        self.db.execute(update_category)
        self.db.commit()

    def deleteCategory(self, category_id):
        delete_category = "DELETE FROM categories WHERE id = %d ;" % (category_id)
        self.db.execute(delete_category)
        self.db.commit()

    def addCategory(self, category):
        table_not_exist = "CREATE TABLE IF NOT EXISTS categories("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "description TEXT NOT NULL);"
        self.db.execute(table_not_exist)
        self.db.commit()
        cursor = self.db.execute("SELECT id FROM categories ORDER BY id \
                                DESC LIMIT 1;")
        last_id = None
        for row in cursor:
            last_id = int(row[0])
            break
        if last_id != None:
            category_id = last_id + 1
        else:
            category_id =  0
        self.db.execute("INSERT INTO categories (id, description)\
                        VALUES (?,?);" , (category_id, category.description))
        self.db.commit()
