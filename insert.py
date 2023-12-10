from base import Session, engine, Base
from customer import Customer
from review import Review
from restaurant import Restaurant

Base.metadata.create_all(engine)
session = Session()

# create Customers
bob = Customer(first_name="Bob", last_name="Smith")
ted = Customer(first_name = "Ted", last_name = "Kelvin")
session.add(bob)
session.add(ted)

session.commit()
session.close()