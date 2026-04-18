from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    appointments = relationship("Appointment", back_populates="barber")


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    appointments = relationship("Appointment", back_populates="client")


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    barber_id = Column(Integer, ForeignKey("barbers.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))

    barber = relationship("Barber", back_populates="appointments")
    client = relationship("Client", back_populates="appointments")