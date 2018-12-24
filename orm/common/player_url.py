from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, BigInteger, String, DateTime

from fantalytix_sqlalchemy.orm.common.audit_entity import AuditEntity

Base = declarative_base()

class PlayerUrl(Base, AuditEntity):
    __tablename__ = 'player_urls'
    __table_args__ = {'schema':'fantalytix'}

    player_id = Column(BigInteger, nullable=False)
    url = Column(String(512), primary_key=True, nullable=False)
    site = Column(String(50), nullable=False)

    def __repr__(self):
        return "<PlayerUrl(url='{url}')>".format(url=self.url[:10])
