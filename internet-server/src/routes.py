from flask import Blueprint, redirect, render_template, session
from flask import current_app as app

main = Blueprint('main', __name__)


def get_style():
    try:
        if session["stylesheet"] is not None:
            stylesheet = session["stylesheet"]
        else:
            stylesheet = app.stylesheet
    except KeyError:
        stylesheet = app.stylesheet
    return stylesheet



@main.route("/")
def accueil():
    game_data = dict()
    #if 'cookies_nbr' in session:
    #    session['cookies_nbr'] += 1
    #else:
    #    session['cookies_nbr'] = 1
    app.cookies += 1
    game_data['cookies_nbr'] = app.cookies  # session['cookies_nbr']
    game_data['upgrades'] = app.upgrades
    return render_template("index.html", stylesheet=get_style(), app_name=app.config["APP_NAME"],
                           game_data=game_data, version=app.version)


@main.route("/buy/<upgrade_name>")
def buy(upgrade_name):
    if upgrade_name in app.upgrades:
        #if app.upgrades[upgrade_name]["cost"] < session["cookies_nbr"]:
        if app.upgrades[upgrade_name]["cost"] < app.cookies:
            #session["cookies_nbr"] -= app.upgrades[upgrade_name]["cost"]
            app.cookies -= app.upgrades[upgrade_name]["cost"]
        else:
            app.logger.info("Not enough cookies")
    else:
        app.logger.info("Upgrade not found")
    return redirect("/")
