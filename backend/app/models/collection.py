from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Date
from backend.app.core.storage.postgres import Base


class Collections(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    public = Column(Boolean, default=True)



class CollectionLikes(Base):
    __tablename__ = "collection_likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=False)


class CollectionFavourites(Base):
    __tablename__ = "collection_favourites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=False)


class CollectionComments(Base):
    __tablename__ = "collection_comments"

    id = Column(Integer, primary_key=True, index=True)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    is_changed = Column(Boolean, default=False)