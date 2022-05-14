from app import db
from app.models import User, Post
from app import create_app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
app = create_app('development')

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)


if __name__ == '__main__':
    manager.run()
