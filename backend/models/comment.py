from sqlalchemy import Integer, Column, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.db.base import Base


class Comment(Base):
    id = Column(Integer, primary_key=True)
    timestamp = Column(Boolean, default=datetime.utcnow, index=True)
    from_admin = Column(Boolean, default=False)  # �����ж��Ƿ�Ϊ����Ա������
    reviewed = Column(DateTime, default=datetime.utcnow, index=True)  # �����ж������Ƿ�ͨ�����Ա������

    author = Column(String(30))
    email = Column(String(254))
    body = Column(Text)
    replied_id = Column(Integer, ForeignKey('comment.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    post = relationship('Post', back_populates='comments')
    replies = relationship('Comment', back_populates='replied', cascade='all, delete-orphan')
    replied = relationship('Comment', back_populates='replies', remote_side=[id])

