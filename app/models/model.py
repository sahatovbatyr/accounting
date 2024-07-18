from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, DECIMAL
from sqlalchemy.orm import relationship, Mapped
from app.database.db_config import Base



users_roles_association = Table(
    'users_roles',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('user_roles.id'))
)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    roles = relationship("UserRole", secondary=users_roles_association)

    class Config:
        from_attributes = True


class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, unique=True, index=True)

    class Config:
        from_attributes = True





class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    assigned_to_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", foreign_keys=[author_id])
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])


class StockDoc(Base):
    __tablename__ = "stock_docs"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True )
    doc_date = Column(Date, nullable=False)
    autor_id : Mapped[int] = Column(Integer, ForeignKey("users.id"), nullable=False)
    doc_number = Column(String(20), nullable=False )
    oper_id: Mapped[int]  = Column(Integer, ForeignKey("stock_operations.id"), nullable=False)
    note = Column(String(150), nullable=False)

    autor = relationship("User", foreign_keys= "[author_id]")
    stock_records = relationship("StockRecord", back_populates="stock_doc", cascade="all, delete-orphan")
    operation = relationship("StockOperation", foreign_keys="[oper_id]", )


class StockOperaton(Base):
    __tablename__ = "stock_operations"
    id = Column(Integer, primary_key=True, index = True)
    oper_type = Column(String(100), unique = True, nullable=False)
    oper_name = Column(String(100), unique = True, nullable=False)

class StockRecord(Base):
    __tablename__ = "stock_records"
    id = Column(Integer, primary_key=True, index=True)
    doc_id = Column(Integer,    ForeignKey("stock_docs.id"), nullable=False  )
    quantity = Column(DECIMAL(14,3), default=0, nullable=False )
    price = Column(DECIMAL(14, 4), default=0, nullable=False)
    note = Column(String(150), nullable=False )

    document = relationship("StockDoc",foreign_keys="[doc_id]" )

