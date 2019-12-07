import logging
from flask import Flask

from src.game_data import GameData
from src.routes import main

import logging


class Application(Flask):
    """
    Flask application for the Application
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.WARNING)
        with open("version.txt", 'r') as f:
            self.version = f.read()
        self.game_data = GameData()

        self.stylesheet = "default.css"
        self.config.from_pyfile("config.py")
        self.register_blueprint(main)
        #self.register_blueprint(auth)
        #self.register_blueprint(playlist)

#app = Jukebox(__name__)
