from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    Time, Float, SmallInteger, PrimaryKeyConstraint)

from orm.common.audit_entity import AuditEntity

Base = declarative_base()

class NBAPlayerAdvancedGameStats(Base, AuditEntity):
    __tablename__ = 'nba_player_advanced_game_stats'
    __table_args__ = (
        PrimaryKeyConstraint(
            'nba_game_id', 
            'player_id', 
            name='nba_player_advanced_game_stats_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    nba_game_id = Column(BigInteger, nullable=False)
    player_id = Column(BigInteger, nullable=False)
    team_id = Column(Integer, nullable=False)
    minutes_played = Column(Time)
    true_shooting_percentage = Column(Float)
    effective_field_goal_percentage = Column(Float)
    three_point_attempt_rate = Column(Float)
    free_throw_attempt_rate = Column(Float)
    offensive_rebound_percentage = Column(Float)
    defensive_rebound_percentage = Column(Float)
    total_rebound_percentage = Column(Float)
    assist_percentage = Column(Float)
    steal_percentage = Column(Float)
    block_percentage = Column(Float)
    turnover_percentage = Column(Float)
    usage_percentage = Column(Float)
    offensive_rating = Column(SmallInteger)
    defensive_rating = Column(SmallInteger)

    def __repr__(self):
        return "<NBAPlayerAdvancedGameStats(nba_game_id={}, player_id='{}')>".format(
            self.nba_game_id, self.player_id)
