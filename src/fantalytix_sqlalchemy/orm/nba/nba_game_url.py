from sqlalchemy import (
    Column, BigInteger, Integer, String, DateTime, PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from ..common.base import Base
from ..common.audit_entity import AuditEntity

class NBAGameUrl(Base, AuditEntity):
    __tablename__ = 'nba_game_urls'
    __table_args__ = (
        PrimaryKeyConstraint(
            'nba_game_id',
            'site', 
            name='nba_game_urls_pkay'),
        {
            'schema':'fantalytix',
        }
    )

    nba_game_id = Column(BigInteger, nullable=False)
    url = Column(String(512), nullable=False)
    site = Column(String(50), nullable=False)
    nba_game = relationship("NBAGame",
        primaryjoin="remote(NBAGame.id)==foreign(NBAGameUrl.nba_game_id)"
    )

    def __repr__(self):
        return "<NBAGameUrl(home_team='{}', game_date='{}', site='{}')>".format(
            self.nba_game.home_team.abbreviation, 
            self.nba_game.get_game_date(),
            self.site
        )
