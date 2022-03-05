from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class CardModel(db.Model):
    id: int
    title: str
    description: str

    __tablename__ = 'cards'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    activity_id = Column(UUID(as_uuid=True), ForeignKey('activities.id'))
