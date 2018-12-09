import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm.common.league import League
from test.settings import CONNECTION

class TestLeagueORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_league(self):
        NBA = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
            creation_date=datetime(2018, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            last_updated_by='pycrawl',
            last_updated_date=datetime(2018, 2, 2, 0, 0, 0, tzinfo=timezone.utc)
        )
        NFL = League(
            name='National Football League',
            abbreviation='Nfl',
            sport='football',
            created_by='jcrawl',
            creation_date=datetime(2017, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            last_updated_by='jcrawl',
            last_updated_date=datetime(2017, 2, 2, 0, 0, 0, tzinfo=timezone.utc)
        )
        self.session.add(NBA)
        self.session.add(NFL)
        test_nba = self.session.query(League).filter_by(
            name='National Basketball Association')
        self.assertTrue(NBA is test_nba.first())
        self.assertEqual(NBA.created_by, 'pycrawl')
        test_nfl = self.session.query(League).filter_by(
            name='National Football League')
        self.assertTrue(NFL is test_nfl.first())
        self.assertEqual(NFL.created_by, 'jcrawl')

if __name__ == '__main__':
    unittest.main()
