from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# 🔥 Many-to-Many (barber <-> service)
barber_service = Table(
    "barber_service",
    Base.metadata,
    Column("barber_id", Integer, ForeignKey("barbers.id")),
    Column("service_id", Integer, ForeignKey("services.id"))
)

# 🔥 One-to-One (Client <-> Profile)
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True)

    client_id = Column(Integer, ForeignKey("clients.id"), unique=True)
    client = relationship("Client", back_populates="profile")


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    profile = relationship("Profile", back_populates="client", uselist=False)
    appointments = relationship("Appointment", back_populates="client")


# 🔥 One-to-Many
class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    appointments = relationship("Appointment", back_populates="barber")

    # Many-to-Many
    services = relationship("Service", secondary=barber_service, back_populates="barbers")


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    barbers = relationship("Barber", secondary=barber_service, back_populates="services")


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)

    barber_id = Column(Integer, ForeignKey("barbers.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))

    barber = relationship("Barber", back_populates="appointments")
    client = relationship("Client", back_populates="appointments")