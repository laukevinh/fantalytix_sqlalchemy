import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm.common.team_url import TeamUrl
from test.settings import CONNECTION

class TestTeamUrlORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def test_team_url(self):
        GSW_url = TeamUrl(
            team_id = 1,
            url = 'https://www.basketball-reference.com/teams/GSW/',
            site = 'basketball-reference',
            created_by='pycrawl',
            creation_date=datetime(2018, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            last_updated_by='pycrawl',
            last_updated_date=datetime(2018, 2, 2, 0, 0, 0, tzinfo=timezone.utc)
        )
    
        PHO_url = TeamUrl(
            team_id = 2,
            url = 'https://www.basketball-reference.com/teams/PHO/',
            site = 'basketball-reference',
            created_by='jcrawl',
            creation_date=datetime(2017, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            last_updated_by='jcrawl',
            last_updated_date=datetime(2017, 2, 2, 0, 0, 0, tzinfo=timezone.utc)
        )

        self.session.add(GSW_url)
        self.session.add(PHO_url)

        test_gsw = self.session.query(TeamUrl).filter_by(
            url='https://www.basketball-reference.com/teams/GSW/')
        self.assertTrue(GSW_url is test_gsw.first())
        self.assertEqual(GSW_url.created_by, 'pycrawl')

        test_phx = self.session.query(TeamUrl).filter_by(
            url='https://www.basketball-reference.com/teams/PHO/')
        self.assertTrue(PHO_url is test_phx.first())
        self.assertEqual(PHO_url.created_by, 'jcrawl')

if __name__ == '__main__':
    unittest.main()
