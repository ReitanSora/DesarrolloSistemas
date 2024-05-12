from config import config
from src import init_app, page_not_found

configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run()
