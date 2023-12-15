from models import Customer, Review
from main  import session
Allcustomers = session.query(Customer).all()
print(Allcustomers)

for customer in Allcustomers:
    print(customer.full_name())
print("")  

Allreviews = session.query(Review).all()

for review in Allreviews:
    print(review.full_review())

restaurantreview = session.query(Review).all()

for review in restaurantreview:
    print(review.full_review())

    