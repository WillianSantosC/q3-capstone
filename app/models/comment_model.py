from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from sqlalchemy import TEXT, Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class CommentModel(db.Model):
    id: int
    hour: str
    comment: str
    user_id: str
    group_id: str

    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    comment = Column(TEXT, nullable=False)
    hour = Column(DateTime, default=datetime.now())
