from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class CardModel(db.Model):
    id: int
    tile: str
    description: str

    __tablename__ = "cards"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    tile = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)
