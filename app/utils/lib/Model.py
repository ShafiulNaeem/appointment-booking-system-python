from db.Database import Database

class Model(Database):
    __table = None
    __primary_key = "id"

    def __init__(self):
        super().__init__()
        self.connect()
        self._select = "*"
        self._wheres = []
        self._order_by = ""
        self._limit = ""
        self._offset = ""
        

    def select(self, *columns):
        self._select = ", ".join(columns) if columns else "*"
        return self

    def where(self, column, operator, value):
        self._wheres.append((column, operator, value))
        return self

    def order_by(self, column, direction="ASC"):
        self._order_by = f"ORDER BY {column} {direction.upper()}"
        return self

    def limit(self, count):
        self._limit = f"LIMIT {count}"
        return self

    def offset(self, count):
        self._offset = f"OFFSET {count}"
        return self

    def get(self):
        where_clause = ""
        values = []

        if self._wheres:
            conditions = [f"{col} {op} %s" for col, op, val in self._wheres]
            where_clause = "WHERE " + " AND ".join(conditions)
            values = [val for _, _, val in self._wheres]

        sql = f"SELECT {self._select} FROM {self.table} {where_clause} {self._order_by} {self._limit} {self._offset}".strip()
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()
    
    def pluck(self, column):
        self.select(column)
        results = self.get()
        return [row[column] for row in results]

    def all(self):
        query = f"SELECT * FROM {self.__table}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def find(self, id):
        query = f"SELECT * FROM {self.__table} WHERE {self.__primary_key} = %s"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()
    
    def create(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.__table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def insert(self, data):
        columns = tuple(data[0].keys())
        placeholders = ", ".join(["%s"] * len(columns))
        columns = ', '.join(columns)
        values= tuple([tuple(item.values()) for item in data])

        query = f"INSERT INTO {self.__table} ({columns}) VALUES ({placeholders})"
        self.cursor.executemany(query, values)
        self.conn.commit()
        return self.cursor.rowcount
    
    def update(self, id, data):
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {self.__table} SET {set_clause} WHERE {self.__primary_key} = %s"
        self.cursor.execute(query, (*data.values(), id))
        self.conn.commit()
        return self.cursor.rowcount
    
    def delete(self, id):
        query = f"DELETE FROM {self.__table} WHERE {self.__primary_key} = %s"
        self.cursor.execute(query, (id,))
        self.conn.commit()
        return self.cursor.rowcount
    

