import psycopg2
import config

class PostgreSQL():
    def __init__(self):
        pass
    
    def connection(self):
        return psycopg2.connect(
            user = config.user,
            password = config.password,
            host = config.host,
            port = config.port,
            dbname = config.db
        )
        
    def select(self, query):
        postgres = self.connection()
        pgcursor = postgres.cursor()
        
        pgcursor.execute(query)
        data = pgcursor.fetchall() # return all tuple data
        postgres.close()
        
        return data
    
    def insert(self, query):
        postgres = self.connection()
        pgcursor = postgres.cursor()
        
        pgcursor.execute(query)
        postgres.commit()
        postgres.close()
        
        return True
    
    def update(self, query):
        postgres = self.connection()
        pgcursor = postgres.cursor()
        
        pgcursor.execute(query)
        postgres.commit()
        postgres.close()
        
        return True
    
    def delete(self, query):
        postgres = self.connection()
        pgcursor = postgres.cursor()
        
        pgcursor.execute(query)
        postgres.commit()
        postgres.close()
        
        return True
