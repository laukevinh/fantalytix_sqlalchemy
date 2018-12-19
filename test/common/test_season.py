"""This is a test for the Season ORM. 

The current database configuration does not have foreign key relationships 
established, so joins are performed explicitly.

Tried to establish the join relationship during ORM definition, but 
that was throwing errors so they are just performed manually each time.
"""
import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from orm.common.league import League
from orm.common.season import Season
from test.settings import CONNECTION

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
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(league)
        self.session.commit()

        season = Season(
            league_id=league.id,
            start_date=date(2018, 10, 16),
            end_date=date(2019, 4, 10),
            start_year=date(2018, 1, 1),
            end_year=date(2019, 1, 1),
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(season)
        self.session.commit()

if __name__ == '__main__':
    unittest.main()
