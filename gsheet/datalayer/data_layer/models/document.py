from data_layer.models.base import Base
import sqlalchemy as sql
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

class Document(Base):
    __tablename__ = 'document'
    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String, unique=True)
    docs = sql.Column(JSON)
    doc_name = sql.Column(sql.String)
    created_at = sql.Column(sql.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Sheet (id={self.id}, title={self.title})>"