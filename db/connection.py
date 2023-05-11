import mysql.connector
import config

class PosgresSQL():
    def __init__(self):
        pass
    
    def connection(self):
        return mysql.connector.connect(
            username = config.user,
            password = config.password,
            host = config.host,
            port = config.port,
            database = config.db,
            connect_timeout = 1000
        )
    
    def sql_select():
        pass
    def sql_insert():
        pass
    