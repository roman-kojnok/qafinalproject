#!/usr/bin/python
from main import create_app
from main.blueprints.page import page
from main.blueprints.page import calc

if __name__ == '__main__':
    app = create_app('flask.cfg')
    app.register_blueprint(page)
    app.register_blueprint(calc)
    app.run(host='0.0.0.0')
