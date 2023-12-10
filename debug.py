from customer import Customer
from base import Session

session = Session()

Allcustomers = session.query(Customer).all()
print(Allcustomers)

for customer in Allcustomers:
    print(customer.full_name())
print("")   
