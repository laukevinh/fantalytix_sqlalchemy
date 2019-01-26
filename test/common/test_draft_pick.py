import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import Player
from fantalytix_sqlalchemy.orm.common import Team
from fantalytix_sqlalchemy.orm.common import League
from fantalytix_sqlalchemy.orm.common import Season
from fantalytix_sqlalchemy.orm.common import DraftPick
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
        )
        self.session.add(player)

        team = Team(
            name='Golden State Warriors',
            abbreviation='GSW',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(team)

        league = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(league)
        self.session.commit()

        season = Season(
            league=league,
            start_date=date(2018, 10, 16),
            end_date=date(2019, 4, 10),
            start_year=date(2018, 1, 1),
            end_year=date(2019, 1, 1),
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(season)
        self.session.commit()

        draft_pick = DraftPick(
            season=season,
            round=1,
            pick_in_round=28,
            overall_pick=28,
            team=team,
            player=player,
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
        )
        self.session.add(draft_pick)
        self.session.commit()

        self.assertIs(draft_pick.season, self.session.query(Season).one())
        self.assertIs(draft_pick.team, self.session.query(Team).one())
        self.assertIs(draft_pick.player, self.session.query(Player).one())

if __name__ == '__main__':
    unittest.main()
