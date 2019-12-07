class GameData:

    def __init__(self):
        self.cookies = 0
        self.upgrades = [
            {'name': "🦖 Raptors", 'base_cost': 100, 'number': 0, 'cpc': 1},
            {'name': "🚌 Autobus", 'base_cost': 1000, 'number': 0, 'cpc': 10}
        ]

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
