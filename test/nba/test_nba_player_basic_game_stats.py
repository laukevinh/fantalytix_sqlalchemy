"""This is a test for the NBA Player Basic Game States. 
configuration does not have foreign key relationships established, so
joins are performed explicitly.

Tried to establish the join relationship during ORM definition, but 
that was throwing errors so they are just performed manually each time.
"""
import unittest

from datetime import date, datetime, timezone, time

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from orm.nba.nba_player_basic_game_stats import NBAPlayerBasicGameStats
from orm.common.player import Player
from orm.common.team import Team
from orm.common.league import League
from orm.common.season import Season
from orm.nba.nba_game import NBAGame
from test.settings import CONNECTION

class TestNBAPlayerBasicGameStatsORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(NBAPlayerBasicGameStats).delete()
        self.session.query(Player).delete()
        self.session.query(Team).delete()
        self.session.query(NBAGame).delete()
        self.session.commit()
        self.session.close()

    def test_nba_player_basic_game_stats(self):
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

        player = Player(
            name='Kevin Durant',
            height = '6-9',
            weight = 240,
            birthday = date(1988, 9, 29),
            birthplace = 'in Washington, District of Columbia',
            nationality = 'us',
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(player)

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

        nba_game = NBAGame(
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
        self.session.add(nba_game)

        self.session.commit()

        player_basic_game_stats = NBAPlayerBasicGameStats(
            nba_game_id=nba_game.id,
            player_id=player.id,
            team_id=teamA.id,
            is_starter=True,
            minutes_played=time(minute=33, second=59),
            field_goals_made=9,
            field_goals_attempted=16,
            field_goal_percentage=0.563,
            three_pointers_made=4,
            three_pointers_attempted=7,
            three_point_percentage=0.571,
            free_throws_made=3,
            free_throws_attempted=4,
            free_throw_percentage=0.750,
            offensive_rebounds=0,
            defensive_rebounds=10,
            total_rebounds=10,
            assists=9,
            steals=1,
            blocks=2,
            turnovers=4,
            personal_fouls=1,
            points=25,
            plus_minus=22,
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(player_basic_game_stats)
        self.session.commit()

if __name__ == '__main__':
    unittest.main()
