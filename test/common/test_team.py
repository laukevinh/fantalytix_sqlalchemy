import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.team import Team
from fantalytix_sqlalchemy.test.settings import CONNECTION

class TestTeamORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_team(self):
        GSW = Team(
            name = 'Golden State Warriors',
            abbreviation= 'GSW',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
    

        PHO = Team(
            name = 'Phoenix Suns',
            abbreviation= 'PHO',
            status='active',
            created_by='jcrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )

        self.session.add(GSW)
        self.session.add(PHO)

        test_gsw = self.session.query(Team).filter_by(
            name='Golden State Warriors')
        self.assertTrue(GSW is test_gsw.first())
        self.assertEqual(GSW.created_by, 'pycrawl')

        test_phx = self.session.query(Team).filter_by(
            name='Phoenix Suns')
        self.assertTrue(PHO is test_phx.first())
        self.assertEqual(PHO.created_by, 'jcrawl')

if __name__ == '__main__':
    unittest.main()
