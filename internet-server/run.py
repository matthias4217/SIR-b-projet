from src import Jukebox

if __name__ == "__main__":
    # run the flask app
    app = Jukebox(__name__)
    app.run(host=app.config["LISTEN_ADDR"], port=app.config["LISTEN_PORT"])
