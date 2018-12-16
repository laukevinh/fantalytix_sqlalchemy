from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, String, BigInteger, Integer, 
    SmallInteger, Numeric, PrimaryKeyConstraint)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class NBAPlayerSeasonPerGameStats(Base, AuditEntity):
    __tablename__ = 'nba_player_season_per_game_stats'
    __table_args__ = (
        PrimaryKeyConstraint(
            'season',
            'player_id', 
            'team_id',
            name='nba_player_season_per_game_average_stats_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    season = Column(String(15), nullable=False)
    player_id = Column(BigInteger, nullable=False)
    team_id = Column(Integer, nullable=False)
    games_played = Column(SmallInteger)
    games_started = Column(SmallInteger)
    minutes_per_game = Column(Numeric)
    field_goals_made_per_game = Column(Numeric)
    field_goals_attempted_per_game = Column(Numeric)
    three_pointers_made_per_game = Column(Numeric)
    three_pointers_attempted_per_game = Column(Numeric)
    two_point_field_goals_made_per_game = Column(Numeric)
    two_point_field_goals_attempted_per_game = Column(Numeric)
    free_throws_made_per_game = Column(Numeric)
    free_throws_attempted_per_game = Column(Numeric)
    offensive_rebounds_per_game = Column(Numeric)
    defensive_rebounds_per_game = Column(Numeric)
    total_rebounds_per_game = Column(Numeric)
    assists_per_game = Column(Numeric)
    steals_per_game = Column(Numeric)
    blocks_per_game = Column(Numeric)
    turnovers_per_game = Column(Numeric)
    personal_fouls_per_game = Column(Numeric)
    points_per_game = Column(Numeric)

    def __repr__(self):
        return "<NBAPlayerSeasonPerGameStats(nba_game_id={}, player_id='{}')>".format(
            self.nba_game_id, self.player_id)
