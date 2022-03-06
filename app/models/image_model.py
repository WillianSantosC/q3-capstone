from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import TEXT, Column, ForeignKey, LargeBinary

from app.configs.database import db


@dataclass
class ImageModel(db.Model):

    __tablename__ = "images"

    id: str = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(TEXT)
    image = db.Column(LargeBinary)
    mimetype = db.Column(TEXT, nullable=False)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
