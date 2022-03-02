from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class ActivityModel(db.Model):
    id: int
    card_id: str
    timer_total: str
    timer_init: str
    category_id: str

    __tablename__ = 'activities'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    category_id = Column(UUID, ForeignKey('categories.id'))
    card_id = Column(UUID, ForeignKey('cards.id'))
    timer_total = Column(DateTime)
    timer_init = Column(DateTime)
    favorite = Column(Boolean, default=False)
