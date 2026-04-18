print("🚀 NEW VERSION IS RUNNING")
from database import engine, session
from models import Base, Client, Profile, Barber, Service, Appointment

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# 🔥 CREATE
client1 = Client(name="Erlan")
profile1 = Profile(phone="0700123456", client=client1)

barber1 = Barber(name="Azamat")
barber2 = Barber(name="Bek")

service1 = Service(name="Haircut")
service2 = Service(name="Shave")

# Many-to-Many
barber1.services.append(service1)
barber1.services.append(service2)
barber2.services.append(service1)

session.add_all([client1, profile1, barber1, barber2, service1, service2])
session.commit()

# Appointment (One-to-Many)
appointment = Appointment(client=client1, barber=barber1)
session.add(appointment)
session.commit()


# 🔍 READ
print("\n--- ALL CLIENTS ---")
clients = session.query(Client).all()
for c in clients:
    print(c.name)


# 🔍 QUERY BY ID
client = session.get(Client, 1)
print("\nClient by ID:", client.name)


# 🔍 QUERY BY FIELD
barber = session.query(Barber).filter_by(name="Azamat").first()
print("\nBarber found:", barber.name)


# 🔍 RELATION QUERY
print("\n--- Barber services ---")
for s in barber.services:
    print(s.name)


# 🔍 FILTER THROUGH RELATION
print("\n--- Barbers who do Haircut ---")
service = session.query(Service).filter_by(name="Haircut").first()
for b in service.barbers:
    print(b.name)


# 🔧 UPDATE
client.name = "Erlan Updated"
session.commit()
print("\nUpdated client:", client.name)


# ❌ DELETE
session.delete(barber2)
session.commit()
print("\nBarber Bek deleted")