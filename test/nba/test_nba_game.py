import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import League, Team, Season
from fantalytix_sqlalchemy.orm.nba import NBAGame
from ..settings import CONNECTION

class TestNBAGameORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(League).delete()
        self.session.query(Team).delete()
        self.session.query(Season).delete()
        self.session.query(NBAGame).delete()
        self.session.commit()
        self.session.close()

    def test_nba_game(self):
        teamA = Team(
            name='Golden State Warriors',
            abbreviation='GSW',
            status='active',
            created_by='pycrawl',
        )
        self.session.add(teamA)

        teamB = Team(
            name='Cleveland Cavaliers',
            abbreviation='CLE',
            status='active',
            created_by='pycrawl',
        )
        self.session.add(teamB)

        league = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
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
        )
        self.session.add(season)
        self.session.commit()

        nba_game= NBAGame(
            season=season,
            home_team=teamB,
            away_team=teamA,
            game_date=datetime(2018, 12, 5, 19, 0, 0, tzinfo=timezone.utc),
            home_score=105,
            away_score=129,
            overtimes=0,
            winning_team=teamA,
            status='scheduled',
            type='season',
            created_by='pycrawl',
        )
        self.session.add(nba_game)
        self.session.commit()

        self.assertIs(
            self.session.query(NBAGame).filter_by(winning_team=teamA).one(), 
            nba_game
        )

if __name__ == '__main__':
    unittest.main()
