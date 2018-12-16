"""This is a test for the DraftPick ORM. 

The current database configuration does not have foreign key relationships 
established, so joins are performed explicitly.

Tried to establish the join relationship during ORM definition, but 
that was throwing errors so they are just performed manually each time.
"""
import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from orm.common.player import Player
from orm.common.team import Team
from orm.common.draft_pick import DraftPick
from test.settings import CONNECTION

class TestDraftPickORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(Player).delete()
        self.session.query(Team).delete()
        self.session.query(DraftPick).delete()
        self.session.commit()
        self.session.close()

    def test_draft_pick(self):
        player = Player(
            name='Jacob Evans',
            height = '6-6',
            weight = 210,
            birthday = date(1997, 6, 18),
            birthplace = 'in Jacksonville, North Carolina',
            nationality = 'us',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(player)

        team = Team(
            name='Golden State Warriors',
            abbreviation='GSW',
            status='active',
            league='NBA',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(team)
        self.session.commit()

        draft_pick = DraftPick(
            year=date(2018, 6, 21),
            round=1,
            pick=28,
            team_id=team.id,
            player_id=player.id,
            league='NBA',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(draft_pick)
        self.session.commit()

if __name__ == '__main__':
    unittest.main()
