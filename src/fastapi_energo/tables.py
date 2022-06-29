from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Index
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Device(Base):
    __tablename__ = "devices"

    id = Column(BigInteger, primary_key=True)
    dev_id = Column(String(200), nullable=False)
    dev_type = Column(String(120), nullable=False)


Index('devices_dev_id_dev_type_index', Device.dev_id, Device.dev_type)


class Endpoint(Base):
    __tablename__ = "endpoints"

    id = Column(BigInteger, primary_key=True)
    device_id = Column(
        Integer, ForeignKey("devices.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    comment = Column(String)
