import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import Team
from fantalytix_sqlalchemy.orm.common import TeamUrl
from ..settings import CONNECTION

class TestTeamUrlORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(Team).delete()
        self.session.query(TeamUrl).delete()
        self.session.commit()
        self.session.close()

    def test_team_url(self):
        team = Team(
            name = 'Golden State Warriors',
            abbreviation= 'GSW',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(team)
        self.session.commit()

        team_url = TeamUrl(
            team=team,
            url='https://www.basketball-reference.com/teams/GSW/',
            site='basketball-reference',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(team_url)
        self.session.commit()

        self.assertIs(self.session.query(TeamUrl).one().team, team)

if __name__ == '__main__':
    unittest.main()
