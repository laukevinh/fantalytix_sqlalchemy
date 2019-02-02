"""Helper object to include four audit columns common among all tables.
server_default is used for creation_date but not last_updated intentionally. 
See the explanations below:

https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
https://docs.sqlalchemy.org/en/latest/core/defaults.html#server-side-defaults

Note that creation_date's db schema must also have 
DEFAULT (now() at time zone 'utc') for server_default=func.now() to work.
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from datetime import datetime

class AuditEntity:

    created_by = Column(String(255))

    """3 options for creation_date"""

    """Option 1: if schema definition does not have default NOW, use"""
    creation_date = Column(DateTime(timezone=True), default=datetime.utcnow)
    """Option 2: if schema definition has default NOW, use"""
    # creation_date = Column(DateTime(timezone=True), server_default=func.utc_timestamp())
    """Option 3: same effect as option 2"""
    # creation_date = Column(DateTime(timezone=True), server_default=func.now())

    last_updated_by = Column(String(255))

    """Only 1 valid option for last_updated_date"""
    last_updated_date = Column(DateTime(timezone=True), onupdate=datetime.utcnow)

    """onupdate=func.now() returns date 8 hours behind"""
    """server_onupdate=func.now() returns none"""
    """server_onupdate=func.utc_timestamp() returns none"""

    def __repr__(self):
        return (
            "<AuditEntity("
                "created_by='{}', "
                "creation_date='{}'"
            ")>".format(
                self.created_by, 
                self.creation_date.date()
            )
        )
