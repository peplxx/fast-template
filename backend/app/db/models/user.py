import sqlalchemy as sa
from sqlalchemy import Column
from sqlalchemy.orm import Mapped

from .mixins.index import UUIDMixin
from .. import DeclarativeBase as Base


class User(UUIDMixin, Base):
    """Basic user model"""

    __tablename__ = "users"
    password: Mapped[str] = Column(sa.String(255), nullable=False)
    username: Mapped[str] = Column(sa.String(255), nullable=False)
