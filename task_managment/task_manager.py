from sqlalchemy import String,engine,create_engine,ForeignKey,Integer
from sqlalchemy.orm import DeclarativeBase,sessionmaker,relationship,Mapped,mapped_column
from sqlalchemy.exc import IntegrityError
from typing import List

class Base(DeclarativeBase):
    pass
engine=create_engine("mysql+pymysql://root:root@127.0.0.1:3306/task_management")
Session=sessionmaker(bind=engine)
session=Session()

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    username:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)
    password:Mapped[str]=mapped_column(String(50),nullable=False)
    tasks:Mapped[List["Task"]]=relationship(back_populates="user")
    categories:Mapped[List["Category"]]=relationship(back_populates="user")
    comments:Mapped[List["Comment"]]=relationship(back_populates="user")


class Task(Base):
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(50),nullable=False)
    description:Mapped[str]=mapped_column(String(50),nullable=False)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    user:Mapped["User"]=relationship(back_populates="tasks")
    tag_id:Mapped[int]=mapped_column(ForeignKey("tags.tag_id"),nullable=False)
    tags:Mapped["Tag"]=relationship(back_populates="tasks")
    category_id:Mapped[str]=mapped_column(ForeignKey("categories.id"),nullable=False)
    category:Mapped["Category"]=relationship(back_populates="tasks")
    comments:Mapped[list["Comment"]]=relationship(back_populates="tasks")

class Category(Base):
    __tablename__="categories"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    type:Mapped[str]=mapped_column(String(50),nullable=False)
    tasks:Mapped[List["Task"]]=relationship(back_populates="categories")
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    user:Mapped["User"]=relationship(back_populates="categories")



class Comment(Base):
    __tablename__="comments"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=True)
    user:Mapped["User"]=relationship(back_populates="comments")
    taks_id:Mapped[int]=mapped_column(ForeignKey("tasks.id"),nullable=True)
    task:Mapped["Task"]=relationship(back_populates="comments")

class Tag(Base):
    __tablename__="tags"
    tag_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    tag_name:Mapped[str]=mapped_column(String(50),nullable=False)
    tasks:Mapped[List["Task"]]=relationship(back_populates="tags")

Base.metadata.create_all(engine)
