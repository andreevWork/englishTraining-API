from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import myApp, myDb
from index import start_server

# Нужно чтобы подцепились модели для миграций
from models.serials import Serial

manager = Manager(myApp)
migrate = Migrate(myApp, myDb)

manager.add_command('db', MigrateCommand)


@manager.command
def start():
    start_server()


if __name__ == "__main__":
    manager.run()
