from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone

from ..database.core import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    full_name = Column(String, nullable=False, index=True)
    password_hash = Column(String, nullable=False, index=True)
    role = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"""
            User(
                id={self.id},
                email={self.email},
                full_name={self.full_name},
                role={self.role},
                created_at={self.created_at},
                active={self.active}
            )
        """