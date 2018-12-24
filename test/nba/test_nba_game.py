"""This is a test for the NBAGame and Team ORMs. The current database 
configuration does not have foreign key relationships established, so
joins are performed explicitly.

Tried to establish the join relationship during ORM definition, but 
that was throwing errors so they are just performed manually each time.
"""
import unittest

from datetime import date, datetime, timezone

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common.team import Team
from fantalytix_sqlalchemy.orm.common.league import League
from fantalytix_sqlalchemy.orm.common.season import Season
from fantalytix_sqlalchemy.orm.nba.nba_game import NBAGame
from fantalytix_sqlalchemy.orm.nba.nba_game_url import NBAGameUrl
from fantalytix_sqlalchemy.test.settings import CONNECTION

class TestTeamNBAGameORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(Team).delete()
        self.session.query(NBAGame).delete()
        self.session.query(NBAGameUrl).delete()
        self.session.commit()
        self.session.close()

    def test_team_nba_game(self):
        teamA = Team(
            name='Golden State Warriors',
            abbreviation='GSW',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(teamA)

        teamB = Team(
            name='Cleveland Cavaliers',
            abbreviation='CLE',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(teamB)

        teamC = Team(
            name='San Antonio Spurs',
            abbreviation='SAS',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(teamC)

        teamD = Team(
            name='Los Angeles Lakers',
            abbreviation='LAL',
            status='active',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(teamD)

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

        nba_game_1 = NBAGame(
            season_id=season.id,
            home_team_id=teamB.id,
            away_team_id=teamA.id,
            game_date=datetime(2018, 12, 5, 19, 0, 0, tzinfo=timezone.utc),
            home_score=105,
            away_score=129,
            overtimes=0,
            winning_team_id=teamA.id,
            status='scheduled',
            type='season',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(nba_game_1)

        nba_game_2 = NBAGame(
            season_id=season.id,
            home_team_id=teamD.id,
            away_team_id=teamC.id,
            game_date=datetime(2018, 12, 5, 20, 30, 0, tzinfo=timezone.utc),
            home_score=121,
            away_score=113,
            overtimes=0,
            winning_team_id=teamD.id,
            status='scheduled',
            type='season',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(nba_game_2)

        self.session.commit()

        nbagame_url = NBAGameUrl(
            nba_game_id=nba_game_1.id,
            url = ('https://www.basketball-reference.com/'
                   'boxscores/201812050CLE.html'),
            site = 'basketball-reference',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(nbagame_url)
        self.session.commit()

        """ example query notation 1
            Get list of home_team, nba_game tuples that played on 12/5/2018
        """
        for home_team, nba_game in self.session.query(Team, NBAGame).\
                filter(Team.id==NBAGame.home_team_id).\
                filter(cast(NBAGame.game_date, Date)==date(2018, 12, 5)).\
                all():
            self.assertTrue(home_team in [teamB, teamD])
            self.assertTrue(nba_game in [nba_game_1, nba_game_2])

        """ example query notation 2
            Get list of all home teams that played on 12/5/2018
        """
        test_teams = self.session.query(Team).\
            join(NBAGame, Team.id==NBAGame.home_team_id).\
            filter(cast(NBAGame.game_date, Date)==date(2018, 12, 5)).\
            all()
        self.assertTrue(teamB in test_teams)
        self.assertTrue(teamD in test_teams)

if __name__ == '__main__':
    unittest.main()
