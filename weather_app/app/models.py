from app import db


class WeatherReport(db.Model):
    id_log =  db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return "<id_log={} and station={}>".format(self.id_log, self.station)

