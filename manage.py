"""
System file to manage the utility commands
"""
from flask import current_app
from flask_script import Shell, Manager

from app.app import create_app


def _create_manager_obj(application):
    """
    Method to create one manager object
    """
    manager_obj = Manager(application, with_default_commands=False)
    manager_obj.add_command("shell", Shell)

    return manager_obj


flask_app = create_app()
manager = _create_manager_obj(flask_app)


@manager.command
def run():
    """
    Runs the api server
    """
    port = int(current_app.config["PORT"])
    host = current_app.config["HOST"]
    debug = current_app.config["DEBUG"]

    current_app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    manager.run()
