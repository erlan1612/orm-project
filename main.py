from database import engine, session
from models import Base, Barber, Client, Appointment

# создаём таблицы
Base.metadata.create_all(engine)

# добавляем данные
barber1 = Barber(name="Azamat")
client1 = Client(name="Erlan")

session.add(barber1)
session.add(client1)
session.commit()

# создаём запись
appointment = Appointment(barber=barber1, client=client1)
session.add(appointment)
session.commit()

# выводим данные
appointments = session.query(Appointment).all()

for a in appointments:
    print(f"Barber: {a.barber.name}, Client: {a.client.name}")