from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database.db_config import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    roles = relationship("UserRole", back_populates="users")

class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, unique=True, index=True)


users_roles_association = Table(
    'users_roles',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('user_roles.id'))
)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    assigned_to_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", foreign_keys=[author_id])
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])




