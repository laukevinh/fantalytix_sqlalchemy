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

from fantalytix_sqlalchemy.orm.common.player import Player
from fantalytix_sqlalchemy.orm.common.team import Team
from fantalytix_sqlalchemy.orm.common.league import League
from fantalytix_sqlalchemy.orm.common.season import Season
from fantalytix_sqlalchemy.orm.common.draft_pick import DraftPick
from ..settings import CONNECTION

class TestDraftPickORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(Player).delete()
        self.session.query(Team).delete()
        self.session.query(League).delete()
        self.session.query(Season).delete()
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
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(team)

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

        draft_pick = DraftPick(
            season_id=season.id,
            round=1,
            pick_in_round=28,
            overall_pick=28,
            team_id=team.id,
            player_id=player.id,
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(draft_pick)
        self.session.commit()

if __name__ == '__main__':
    unittest.main()
