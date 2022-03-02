import re
from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db
from app.services.exceptions import EmailError


@dataclass
class UserModel(db.Model):
    name: str
    email: str

    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(64), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(64), nullable=False)
    image_id = Column(UUID, ForeignKey('images.id'))
    activity_id = Column(UUID, ForeignKey('activities.id'))

    @property
    def password(self):
        raise AttributeError('Password is not accessible')

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @validates('email')
    def validate_email(self, _, value):
        regex = '(?:[a-z0-9!#$%&"*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&"*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'

        email = re.fullmatch(regex, value)

        if not email:
            raise EmailError()

        return value
