from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class ActivityModel(db.Model):
    id: int
    timer_total: str
    timer_init: str
    favorite: bool

    __tablename__ = 'activities'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'))
    timer_total = Column(String, default='00:00:00')
    timer_init = Column(String)
    favorite = Column(Boolean, default=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    category: list = db.relationship('CategoryModel', backref='activities')
    card: list = db.relationship('CardModel', backref='activities')
