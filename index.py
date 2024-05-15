from config import config
from src import init_app, page_not_found


def initialize_app():
    configuration = config['development']
    app = init_app(configuration)

    return app


if __name__ == '__main__':
    app = initialize_app()
    app.register_error_handler(404, page_not_found)
    app.run()
