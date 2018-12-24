from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    Boolean, Time, SmallInteger, Float, PrimaryKeyConstraint)

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

class NBAPlayerBasicGameStats(Base, AuditEntity):
    __tablename__ = 'nba_player_basic_game_stats'
    __table_args__ = (
        PrimaryKeyConstraint(
            'nba_game_id', 
            'player_id', 
            name='nba_player_basic_game_stats_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    nba_game_id = Column(BigInteger, nullable=False)
    player_id = Column(BigInteger, nullable=False)
    team_id = Column(Integer, nullable=False)
    is_starter = Column(Boolean)
    minutes_played = Column(Time)
    field_goals_made = Column(SmallInteger)
    field_goals_attempted = Column(SmallInteger)
    field_goal_percentage = Column(Float)
    three_pointers_made = Column(SmallInteger)
    three_pointers_attempted = Column(SmallInteger)
    three_point_percentage = Column(Float)
    free_throws_made = Column(SmallInteger)
    free_throws_attempted = Column(SmallInteger)
    free_throw_percentage = Column(Float)
    offensive_rebounds = Column(SmallInteger)
    defensive_rebounds = Column(SmallInteger)
    total_rebounds = Column(SmallInteger)
    assists = Column(SmallInteger)
    steals = Column(SmallInteger)
    blocks = Column(SmallInteger)
    turnovers = Column(SmallInteger)
    personal_fouls = Column(SmallInteger)
    points = Column(SmallInteger)
    plus_minus = Column(SmallInteger)

    def __repr__(self):
        return "<NBAPlayerBasicGameStats(nba_game_id={}, player_id='{}')>".format(
            self.nba_game_id, self.player_id)
