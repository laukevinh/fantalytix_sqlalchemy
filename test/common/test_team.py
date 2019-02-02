import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import Team
from ..settings import CONNECTION

class TestTeamORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(Team).delete()
        self.session.commit()
        self.session.close()

    def test_team(self):
        team = Team(
            name = 'Golden State Warriors',
            abbreviation= 'GSW',
            status='active',
            created_by='pycrawl',
        )
        self.session.add(team)
        self.assertIs(self.session.query(Team).one(), team)

if __name__ == '__main__':
    unittest.main()
