"""Helper object for the four audit columns
common amongst all fantalytix tables.
"""

from sqlalchemy import Column, String, DateTime

class Audit:

    created_by = Column(String(255))
    creation_date = Column(DateTime)
    last_updated_by = Column(String(255))
    last_updated_date = Column(DateTime)

    def __repr__(self):
        return "<Audit(object)>"
