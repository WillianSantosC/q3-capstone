from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class CategoryModel(db.Model):
    name: str

    __tablename__ = 'categories'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(64), nullable=False, unique=True)
