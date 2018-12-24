import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.team_url import TeamUrl
from fantalytix_sqlalchemy.test.settings import CONNECTION

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
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
    
        PHO_url = TeamUrl(
            team_id = 2,
            url = 'https://www.basketball-reference.com/teams/PHO/',
            site = 'basketball-reference',
            created_by='jcrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
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
