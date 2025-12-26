from sqlalchemy import create_engine, text


class Species_type:
    scripts = {
        "select all": "SELECT * FROM species_type",
        "select by id": "SELECT * FROM species_type WHERE type_id = :id",
        "insert": "INSERT INTO species_type(\"type_id\",\"type_name\")\
            VALUES (:cr_id, :cr_name)",
        "update": "UPDATE species_type SET type_name = :new_name\
            WHERE type_id = :ex_id",
        "delete": "DELETE FROM species_type WHERE type_id = :del_id"
        }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_species_type(self):
        connection = self.db.connect()
        rows = connection.execute(text(self.scripts
                                  ["select all"])).mappings().all()
        connection.close()
        return rows

    def get_species_type_by_id(self, type_id):
        connection = self.db.connect()
        row = connection.execute(text(self.scripts
                                 ["select by id"]),
                                 {"id": type_id}).mappings().all()
        connection.close()
        return row

    def create_species_type(self, create_id, create_name):
        self.create_id = create_id
        self.create_name = create_name
        connection = self.db.connect()
        transaction = connection.begin()
        connection.execute(text(self.scripts["insert"]),
                           {"cr_id": create_id, "cr_name": create_name})
        transaction.commit()
        connection.close()

    def update_species_type(self, existing_id, new_name):
        self.existing_id = existing_id
        self.new_name = new_name
        connection = self.db.connect()
        transaction = connection.begin()
        connection.execute(text(self.scripts["update"]),
                           {"ex_id": existing_id, "new_name": new_name})
        transaction.commit()
        connection.close()

    def delete_species_type(self, delete_id):
        connection = self.db.connect()
        transaction = connection.begin()
        connection.execute(text(self.scripts["delete"]),
                           {"del_id": delete_id})
        transaction.commit()
        connection.close()
