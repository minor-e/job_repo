from flask import render_template, flash, redirect, url_for
from app import app, db, models
from app.forms import WeatherForm



# decorators
@app.route("/")
@app.route("/index", methods=["GET"])
def index():
    # Welcome phrase
    return render_template("index.html",title="Home")


#decrators
@app.route("/weather", methods=["GET", "POST"])
def weather():
    form = WeatherForm()
    if form.validate_on_submit():
        # Getting StringField data
        station = form.station.data

        # Populating weatherdb database
        wdb = models.WeatherReport(station=station)
        db.session.add(wdb)
        db.session.commit()

        # Alerting User
        flash("Weather station {} has been added in database".format(form.station.data))
        return redirect(url_for("index"))
    return render_template("weather.html", title="Check Weather", form=form)
