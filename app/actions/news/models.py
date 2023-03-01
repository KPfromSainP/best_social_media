from sqlalchemy import Column, Text, text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from ...database import Base


# space for idea

class News(Base):
    __tablename__ = 'news'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    comment = relationship('Comment', back_populates='news', lazy="immediate")
    user = relationship('User', back_populates='news', lazy="immediate")

    # comment = relationship("Comment", backref="news", lazy='joined')
    # user = relationship('User', back_populates='Comment', lazy="immediate")
