from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand, upgrade

from src.app import myApp, myDb
from index import start_server

# Нужно чтобы подцепились модели для миграций НЕ УДАЛЯТЬ
from src.models.serials import Serial
from src.resourses.episodes import Episode

manager = Manager(myApp)
migrate = Migrate(myApp, myDb)

manager.add_command('db', MigrateCommand)


@manager.command
def start():
    upgrade(directory='migrations')
    start_server()


if __name__ == "__main__":
    manager.run()
