import logging
from flask import Flask
from src.routes import main

import logging


class Jukebox(Flask):
    """
    Flask application for the Jukebox
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.WARNING)
        with open("version.txt", 'r') as f:
            self.version = f.read()

        self.cookies = 0
        self.upgrade = {
            'raptor': 0,
            'autobus': 0
        }

        self.stylesheet = "default.css"
        self.config.from_pyfile("config.py")
        self.register_blueprint(main)
        #self.register_blueprint(auth)
        #self.register_blueprint(playlist)

#app = Jukebox(__name__)