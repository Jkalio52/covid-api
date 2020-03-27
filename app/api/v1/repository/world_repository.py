from sqlalchemy import desc

from app.models import Records


class WorldRepository:

    def get_global_count(self):
        date = Records.query.filter(Records.country_iso == "IND").order_by(desc(Records.date)).first().date
        return Records.query.filter(Records.date == date).all()

    def get_global_count_on_date(self, date: str):
        return Records.query.filter(Records.date == date).all()
