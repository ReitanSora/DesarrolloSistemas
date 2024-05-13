from config import config
from src import init_app, page_not_found

def test():
    configuration = config['development']
    app = init_app(configuration)

    return app

if __name__ == '__main__':
    app = test()
    app.register_error_handler(404, page_not_found)
    app.run()
