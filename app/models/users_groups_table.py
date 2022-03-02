from uuid import uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db

users_groups = db.Table(
    'users_groups',
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column('user_id', UUID, ForeignKey('users.id')),
    Column('group_id', UUID, ForeignKey('groups.id')),
)
