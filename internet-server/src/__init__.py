import logging
from flask import Flask

from src.game_data import GameData
from src.routes import main

import logging
import os
import json

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
        self.config.from_pyfile("config.py")
        self.game_data = GameData(upgrades_path=self.config["UPGRADES_PATH"])
        self.stylesheet = "default.css"
        if (os.path.exists(self.config["SAVE_DATA_PATH"])):
            with open(self.config["SAVE_DATA_PATH"], "r") as s:
                data = json.load(s)
                self.game_data = GameData(data["cookies"], data["upgrades"])
        self.register_blueprint(main)
        #self.register_blueprint(auth)
        #self.register_blueprint(playlist)

#app = Jukebox(__name__)
