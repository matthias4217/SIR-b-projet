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
    app.game_data.update_cookies()

    game_data['cookies_nbr'] = app.game_data.cookies  # session['cookies_nbr']
    game_data['upgrades'] = app.game_data.upgrades
    return render_template("index.html", stylesheet=get_style(), app_name=app.config["APP_NAME"],
                           game_data=game_data, version=app.version)


@main.route("/buy/<int:upgrade_index>")
def buy(upgrade_index):
    # TODO : redo this function
    if upgrade_index >= len(app.game_data.upgrades) | upgrade_index < 0:
        return

    upgrade = app.game_data.upgrades[upgrade_index]
    if upgrade["base_cost"] < app.game_data.cookies:
        app.game_data.cookies -= upgrade["base_cost"]
        upgrade["number"] += 1
    else:
        app.logger.info("Not enough cookies")
    return redirect("/")
