from sqlalchemy.orm import declarative_base, relationship, foreign
from sqlalchemy import Column, Integer, String, ForeignKey
import main

Base = declarative_base()


class Block(Base):
    __tablename__ = 'block'
    block_num = Column(Integer, primary_key=True)
    op = relationship("Operations")


class Operations(Base):
    __tablename__ = "operations"
    block_num = Column(ForeignKey('block.block_num'))
    operation_id = Column(Integer, autoincrement=True, primary_key=True)
    operation_type = Column(String)
    operation_body = Column(String)
    bl = relationship("Block")


# Block.operations = relationship("Operations", order_by=Operations.operation_id, back_populates="block")
Base.metadata.create_all(main.engine)
