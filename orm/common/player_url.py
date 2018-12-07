from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, BigInteger, String, DateTime

Base = declarative_base()

class PlayerUrl(Base):
    __tablename__ = 'player_urls'
    __table_args__ = {'schema':'fantalytix'}

    player_id = Column(BigInteger, nullable=False)
    url = Column(String(512), primary_key=True, nullable=False)
    site = Column(String(50), nullable=False)
    created_by = Column(String(255))
    creation_date = Column(DateTime)
    last_updated_by = Column(String(255))
    last_updated_date = Column(DateTime)

    def __repr__(self):
        return "<PlayerUrl(url='{url}')>".format(url=self.url[:10])
