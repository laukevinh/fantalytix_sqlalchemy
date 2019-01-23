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
        NBA = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(NBA)

        NFL = League(
            name='National Football League',
            abbreviation='NFL',
            sport='football',
            created_by='jcrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(NFL)

        self.session.commit()

if __name__ == '__main__':
    unittest.main()
