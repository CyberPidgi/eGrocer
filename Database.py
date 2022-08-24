import mysql.connector as ms


class Database:
    
    db = None
    cursor = None
    is_connected = False
    
    @classmethod
    def connect(cls, host="localhost", user="root", password="stooby123", database="ShoppingApp"):
        if cls.is_connected:
            return 
        kw = {
        "host": host,
        "user": user,
        "password": password,
        }
        cls.db = ms.connect(**kw)
        cls.cursor = cls.db.cursor()
        
        if database is not None:
            cls.use_database(database)
        
        cls.is_connected = cls.db.is_connected()
        
    @classmethod
    def use_database(cls, database):
        try:
            cls.cursor.execute(f"USE {database};")
        except ms.ProgrammingError:
            choice = input(f"Database {database} does not exist. Create it? (y/n) ")
            if choice == "n":
                raise Exception("Failed to connect to database.")
            cls.create_database(database)
            cls.cursor.execute(f"USE {database};")
    
    @classmethod
    def get_data(cls, table_name):
        cls.cursor.execute(f"SELECT * FROM {table_name};")
        data = cls.cursor.fetchall()
        return data
    
    @classmethod
    def clear_table(cls, table_name):
        cls.cursor.execute(f"DELETE FROM {table_name};")
        cls.db.commit()
    
    @classmethod
    def get_column_names(cls, table_name):
        cls.cursor.execute(f"DESCRIBE {table_name};")
        data = cls.cursor.fetchall()
        return  [record[0] for record in data]
    
    @classmethod 
    def delete_record(cls, table_name, condition):
        cls.cursor.execute(f"DELETE FROM {table_name} WHERE {condition};")
        cls.db.commit()
    
    @classmethod
    def get_specific_data(cls, table_name, column_name, value):
        cls.cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name} = '{value}';")
        data = cls.cursor.fetchone()
        return data
    
    @classmethod
    def insert_data(cls, table_name, new_data):
        command = f"INSERT INTO {table_name} VALUES(" + \
        ",".join(["%s" for _ in range(len(new_data))]) + ");"
        cls.cursor.execute(command, new_data)
        cls.db.commit()
        
    @classmethod
    def update_column(cls, table_name, column_to_set, new_value):
        command = f"UPDATE {table_name} SET {column_to_set} = '{new_value}';"
        cls.cursor.execute(command)
        cls.db.commit()
    
    @classmethod
    def update_column_with_condition(cls, table_name, column_to_set, new_value, condition):
        command = f"UPDATE {table_name} SET {column_to_set} = '{new_value}' WHERE {condition};"
        cls.cursor.execute(command)
        cls.db.commit()
    
    @classmethod
    def get_column_data(cls, table_name, column_name):
        command = f"SELECT {column_name} FROM {table_name};"
        cls.cursor.execute(command)
        return [data[0] for data in cls.cursor.fetchall()]

Database.connect(database="ShoppingAppppp")
