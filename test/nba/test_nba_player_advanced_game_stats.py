"""This is a test for the NBA Player Advanced Game States. 
configuration does not have foreign key relationships established, so
joins are performed explicitly.

Tried to establish the join relationship during ORM definition, but 
that was throwing errors so they are just performed manually each time.
"""
import unittest

from datetime import date, datetime, timezone, time

from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker

from orm.nba.nba_player_advanced_game_stats import NBAPlayerAdvancedGameStats
from orm.common.player import Player
from orm.common.team import Team
from orm.common.league import League
from orm.common.season import Season
from orm.nba.nba_game import NBAGame
from test.settings import CONNECTION

class TestNBAPlayerAdvancedGameStatsORM(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.query(NBAPlayerAdvancedGameStats).delete()
        self.session.query(Player).delete()
        self.session.query(Team).delete()
        self.session.query(NBAGame).delete()
        self.session.commit()
        self.session.close()

    def test_nba_player_advanced_game_stats(self):
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

        player_adv_game_stats = NBAPlayerAdvancedGameStats(
            nba_game_id=nba_game.id,
            player_id=player.id,
            team_id=teamA.id,
            minutes_played=time(minute=33, second=59),
            true_shooting_percentage=0.704,
            effective_field_goal_percentage=0.688,
            three_point_attempt_rate=0.438,
            free_throw_attempt_rate=0.250,
            offensive_rebound_percentage=0,
            defensive_rebound_percentage=28.8,
            total_rebound_percentage=16.2,
            assist_percentage=39.4,
            steal_percentage=1.5,
            block_percentage=5.0,
            turnover_percentage=18.4,
            usage_percentage=29.7,
            offensive_rating=128,
            defensive_rating=105,
            created_by='pycrawl',
            creation_date=datetime.now(tz=timezone.utc),
            last_updated_by=None,
            last_updated_date=None
        )
        self.session.add(player_adv_game_stats)
        self.session.commit()

if __name__ == '__main__':
    unittest.main()
