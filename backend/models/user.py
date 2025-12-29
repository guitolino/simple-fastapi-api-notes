from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from datetime import datetime, timezone

from ..database.core import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), unique=True, nullable=False, index=True)
    title = Column(String, nullable=False, index=True)
    content = Column(Text, nullable=False, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"""
            User(
                id={self.id},
                user_id={self.user_id},
                title={self.title},
                content={self.content},
                created_at={self.created_at}
            )
        """