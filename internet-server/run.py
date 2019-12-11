from src import Application

if __name__ == "__main__":
    # run the flask app
    app = Application(__name__)
    app.run(host=app.config["LISTEN_ADDR"], port=app.config["LISTEN_PORT"])
