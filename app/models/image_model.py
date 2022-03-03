from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import TEXT, Column
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class ImageModel(db.Model):
    id: int
    image: str

    __tablename__ = 'images'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    image = Column(TEXT)
