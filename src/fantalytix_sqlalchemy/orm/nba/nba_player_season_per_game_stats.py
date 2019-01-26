from sqlalchemy import (
    Column, String, BigInteger, Integer, SmallInteger, Numeric, 
    PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from ..common.base import Base
from ..common.audit_entity import AuditEntity

class NBAPlayerSeasonPerGameStats(Base, AuditEntity):
    __tablename__ = 'nba_player_season_per_game_stats'
    __table_args__ = (
        PrimaryKeyConstraint(
            'season_id',
            'player_id', 
            'team_id',
            name='nba_player_season_per_game_average_stats_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    season_id = Column(Integer, nullable=False)
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
    season = relationship("Season",
        primaryjoin=("remote(Season.id)=="
                     "foreign(NBAPlayerSeasonPerGameStats.season_id)")
    )
    player = relationship("Player",
        primaryjoin=("remote(Player.id)=="
                     "foreign(NBAPlayerSeasonPerGameStats.player_id)")
    )
    team = relationship("Team",
        primaryjoin=("remote(Team.id)=="
                     "foreign(NBAPlayerSeasonPerGameStats.team_id)")
    )

    def __repr__(self):
        return (
            "<NBAPlayerSeasonPerGameStats("
                "player='{}', "
                "team='{}', "
                "season='{}'"
            ")>".format(
                self.player.name,
                self.team.abbreviation,
                self.season.pretty_print_years()
            )
        )
