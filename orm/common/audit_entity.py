"""Helper object for the four audit columns
common among all fantalytix tables.
"""

from sqlalchemy import Column, String, DateTime

class AuditEntity:

    created_by = Column(String(255))
    creation_date = Column(DateTime)
    last_updated_by = Column(String(255))
    last_updated_date = Column(DateTime)

    def __repr__(self):
        return "<AuditEntity(object)>"
