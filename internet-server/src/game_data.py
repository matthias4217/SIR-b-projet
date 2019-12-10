import json

class GameData:

    def __init__(self, _cookies = 0, _upgrades = None, upgrades_path = None):
        self.cookies = _cookies
        if (_upgrades == None):
            try:
                with open(upgrades_path, "r") as f:
                    self.upgrades = json.load(f)
            except:
                print("cannot find upgrades file!")
                raise
        else:
            self.upgrades = _upgrades

    def get_cookies_from_click(self):
        new_cookies = 1
        for upgrade in self.upgrades:
            new_cookies += upgrade['number'] * upgrade['cpc']
        return new_cookies

    def update_cookies(self):
        self.cookies += self.get_cookies_from_click()

    def get_json(self):
        return {
            "cookies": self.cookies,
            "upgrades": self.upgrades
        }
