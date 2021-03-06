import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.league import League
from ..settings import CONNECTION

class TestLeagueORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(League).delete()
        self.session.commit()
        self.session.close()

    def test_league(self):
        league = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
        )
        self.session.add(league)
        self.session.commit()
        self.assertEqual(
            self.session.query(League).filter_by(abbreviation='NBA').one(),
            league
        )

        league.abbreviation="nba"
        self.session.add(league)
        self.session.commit()

        self.assertTrue(league.creation_date < league.last_updated_date)

if __name__ == '__main__':
    unittest.main()
