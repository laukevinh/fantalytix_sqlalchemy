from urllib.parse import urlparse

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (Column, BigInteger, Integer, 
    String, DateTime, PrimaryKeyConstraint)

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

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

    def __repr__(self):
        return "<NBAGameUrl(nba_game_id={}, site={})>".format(
            self.nba_game_id, 
            urlparse(self.site).netloc or urlparse(self.site).path
        )
