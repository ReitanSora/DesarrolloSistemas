from src.database.db_connection import get_connection

class DevelopmentConfig():
    DEBUG = True
    SERVER_NAME = '127.0.0.1:4321'
    MYSQL_HOST = ''.join(get_connection()[0])
    MYSQL_PORT = int(''.join(get_connection()[1]))
    MYSQL_USER = ''.join(get_connection()[2])
    MYSQL_PASSWORD = ''.join(get_connection()[3])
    MYSQL_DB = ''.join(get_connection()[4])

config = {
    'development': DevelopmentConfig
}