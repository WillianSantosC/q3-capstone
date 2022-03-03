from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.configs.database import db
from app.models.users_groups_table import users_groups


@dataclass
class GroupModel(db.Model):
    id: str
    title: str
    privacy: bool

    __tablename__ = 'groups'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(64), nullable=False, unique=True)
    privacy = Column(Boolean, default=False)

    users = relationship('UserModel', secondary=users_groups, backref='groups')
