from sqlalchemy import Column, Text, text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from ...database import Base


# space for idea

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    news_id = Column(UUID(as_uuid=True), ForeignKey('news.id'), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())

    # user = relationship('User', back_populates='Comment', lazy="immediate")
    # news = relationship('News', back_populates='Comment', lazy="immediate")
