from urllib.parse import urlparse

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, String, DateTime, 
    PrimaryKeyConstraint)

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

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

    def __repr__(self):
        return "<PlayerUrl(player_id={}, site='{}')>".format(
            self.player_id, self.site)
