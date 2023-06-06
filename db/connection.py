import psycopg2
import config

class PostgresSQL():
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
