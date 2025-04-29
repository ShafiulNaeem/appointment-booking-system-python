from db.Database import Database

class UserMigration(Database):
    def __init__(self):
        super().__init__()
        #self.connect()

    def up(self):
        self.connect()
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    role ENUM('guest', 'host', 'admin') DEFAULT 'guest',
                    name VARCHAR(255) NOT NULL UNIQUE,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    phone VARCHAR(20) NULL,
                    password VARCHAR(255) NOT NULL,
                    address TEXT NULL,
                    image VARCHAR(255) NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
            """)
            self.conn.commit()
            print("Migration up: users table created")
        except Exception as e:
            print(f"Error during migration up: {e}")
        finally:
            self.cursor.close()
            self.conn.close()

    def down(self):
        self.connect()
        try:
            self.cursor.execute("DROP TABLE IF EXISTS users")
            self.conn.commit()
            print("Migration down: users table dropped")
        except Exception as e:
            print(f"Error during migration down: {e}")
        finally:
            self.cursor.close()
            self.conn.close()