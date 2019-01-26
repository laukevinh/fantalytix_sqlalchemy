import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import League
from fantalytix_sqlalchemy.orm.common import Season
from ..settings import CONNECTION

class TestSeasonORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(League).delete()
        self.session.query(Season).delete()
        self.session.commit()
        self.session.close()

    def test_season(self):
        league = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(league)
        self.session.commit()

        season = Season(
            league=league,
            start_date=date(2018, 10, 16),
            end_date=date(2019, 4, 10),
            start_year=date(2018, 1, 1),
            end_year=date(2019, 1, 1),
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc)
        )
        self.session.add(season)
        self.session.commit()

        self.assertIs(
            self.session.query(Season).one().league,
            self.session.query(League).one()
        )

if __name__ == '__main__':
    unittest.main()
