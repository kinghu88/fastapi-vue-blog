from typing import Optional, Tuple
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from backend import crud
from backend.models import Post, Category
from backend.crud.base import CRUDBase
from backend.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):

    def create(self, db: Session, *, obj_in: PostCreate):
        category = crud.category.get(db, id=obj_in.category_id)
        if not category:
            raise ValueError
        db_obj = self.model(
            **obj_in.dict()
        )
        db.add(db_obj)
        db.commit()
        return db_obj

    def get_multi(
            self,
            db: Session,
            *,
            filters: Tuple = tuple(),
            order_by=None,
            page: int = 1,
            limit: int = 10
    ):
        offset = limit * (page - 1)
        query = db.query(
            self.model.id, Post.title, Post.timestamp,
            Post.cover_image, Post.content, Category.name
        ).outerjoin(Post.category)
        if filters:
            query = query.filter(*filters)
        if order_by is not None:
            query = query.order_by(order_by)
        query = query.offset(offset).limit(limit)
        return query.all()


post = CRUDPost(Post)
