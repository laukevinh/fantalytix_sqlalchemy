import unittest

from datetime import date, datetime, timezone, time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fantalytix_sqlalchemy.orm.common import Player, Team, League, Season
from fantalytix_sqlalchemy.orm.nba import (
    NBAGame, NBAPlayerBasicGameStats, NBAPlayerAdvancedGameStats,
    NBAPlayerSeasonPerGameStats
)
from ..settings import CONNECTION

class TestNBAPlayerAllGameStats(unittest.TestCase):
    
    def setUp(self):
        self.engine = create_engine(CONNECTION)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.teamA = Team(
            name='Golden State Warriors',
            abbreviation='GSW',
            status='active',
            created_by='pycrawl',
        )
        self.session.add(self.teamA)

        self.teamB = Team(
            name='Cleveland Cavaliers',
            abbreviation='CLE',
            status='active',
            created_by='pycrawl',
        )
        self.session.add(self.teamB)

        self.player = Player(
            name='Kevin Durant',
            height = '6-9',
            weight = 240,
            birthday = date(1988, 9, 29),
            birthplace = 'in Washington, District of Columbia',
            nationality = 'us',
            created_by='pycrawl',
        )
        self.session.add(self.player)

        league = League(
            name='National Basketball Association',
            abbreviation='NBA',
            sport='basketball',
            created_by='pycrawl',
        )
        self.session.add(league)
        self.session.commit()

        self.season = Season(
            league=league,
            start_date=date(2018, 10, 16),
            end_date=date(2019, 4, 10),
            start_year=date(2018, 1, 1),
            end_year=date(2019, 1, 1),
            created_by='pycrawl',
        )
        self.session.add(self.season)
        self.session.commit()

        self.nba_game = NBAGame(
            season=self.season,
            home_team=self.teamB,
            away_team=self.teamA,
            game_date=datetime(2018, 12, 5, 19, 0, 0, tzinfo=timezone.utc),
            home_score=105,
            away_score=129,
            overtimes=0,
            winning_team=self.teamA,
            status='scheduled',
            type='season',
            created_by='pycrawl',
        )
        self.session.add(self.nba_game)
        self.session.commit()

    def tearDown(self):
        self.session.query(Player).delete()
        self.session.query(Team).delete()
        self.session.query(League).delete()
        self.session.query(Season).delete()
        self.session.query(NBAGame).delete()
        self.session.query(NBAPlayerBasicGameStats).delete()
        self.session.query(NBAPlayerAdvancedGameStats).delete()
        self.session.query(NBAPlayerSeasonPerGameStats).delete()
        self.session.commit()
        self.session.close()

    def test_nba_player_basic_game_stats(self):
        player_basic_game_stats = NBAPlayerBasicGameStats(
            nba_game=self.nba_game,
            player=self.player,
            team=self.teamA,
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
        )
        self.session.add(player_basic_game_stats)
        self.session.commit()

        self.assertIs(
            self.session.query(NBAPlayerBasicGameStats).one().player,
            self.player
        )

    def test_nba_player_advanced_game_stats(self):
        player_adv_game_stats = NBAPlayerAdvancedGameStats(
            nba_game=self.nba_game,
            player=self.player,
            team=self.teamA,
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
        )
        self.session.add(player_adv_game_stats)
        self.session.commit()

        self.assertIs(
            self.session.query(NBAPlayerAdvancedGameStats).one().player,
            self.player
        )

    def test_nba_player_season_per_game_stats(self):
        player_season_per_game_stats = NBAPlayerSeasonPerGameStats(
            season=self.season,
            player=self.player,
            team=self.teamA,
            games_played=68,
            games_started=68,
            minutes_per_game=34.2,
            field_goals_made_per_game=9.3,
            field_goals_attempted_per_game=18.0,
            three_pointers_made_per_game=2.5,
            three_pointers_attempted_per_game=6.1,
            two_point_field_goals_made_per_game=6.7,
            two_point_field_goals_attempted_per_game=11.9,
            free_throws_made_per_game=5.3,
            free_throws_attempted_per_game=5.9,
            offensive_rebounds_per_game=0.5,
            defensive_rebounds_per_game=6.4,
            total_rebounds_per_game=6.8,
            assists_per_game=5.4,
            steals_per_game=0.7,
            blocks_per_game=1.8,
            turnovers_per_game=3.0,
            personal_fouls_per_game=2.0,
            points_per_game=26.4
        )
        self.session.add(player_season_per_game_stats)
        self.session.commit()

        self.assertIs(
            self.session.query(NBAPlayerSeasonPerGameStats).one().player,
            self.player
        )

if __name__ == '__main__':
    unittest.main()
