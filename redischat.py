from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db

from models.user import User
from models.chat import Chat

from routes.index import main as routes_index
from routes.user import main as routes_user

app = Flask(__name__)
db_path = 'chat.sqlite'
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(routes_index)
    app.register_blueprint(routes_user, url_prefix='/user')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        threaded=True,
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
