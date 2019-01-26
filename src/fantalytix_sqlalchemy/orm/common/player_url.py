from sqlalchemy import (
    Column, BigInteger, String, DateTime, PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship, remote, foreign

from .base import Base
from .audit_entity import AuditEntity

class PlayerUrl(Base, AuditEntity):
    __tablename__ = 'player_urls'
    __table_args__ = (
        PrimaryKeyConstraint(
            'player_id',
            'site', 
            name='player_urls_pkey'),
        {
            'schema':'fantalytix',
        }
    )

    player_id = Column(BigInteger, nullable=False)
    site = Column(String(50), nullable=False)
    url = Column(String(512), unique=True, nullable=False)
    player = relationship("Player",
        primaryjoin="remote(Player.id)==foreign(PlayerUrl.player_id)"
    )

    def __repr__(self):
        return "<PlayerUrl(player={}, site='{}')>".format(
            self.player.name, self.site
        )
