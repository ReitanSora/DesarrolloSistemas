from decouple import config


def get_connection():
    try:

        host = config('MYSQL_HOST'),
        port = config('MYSQL_PORT'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD'),
        db = config('MYSQL_DB')
        return host, port, user, password, db

    except Exception as e:
        print(e)
