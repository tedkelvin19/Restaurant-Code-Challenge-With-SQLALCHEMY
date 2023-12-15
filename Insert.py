from models import Customer, Restaurant, Review
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)
customer1 = Customer(first_name="Bob", last_name="Smith")
customer2 = Customer(first_name="Ted", last_name="Kelvin")
customer3 = Customer(first_name="Jim", last_name="Jones")
customer4 = Customer(first_name="Jane", last_name="williams")
customer5 = Customer(first_name="John", last_name="Miller")

restaurant1 = Restaurant(name="McDonalds", price=1000)
restaurant2 = Restaurant(name="KFC", price=3000)
restaurant3 = Restaurant(name="Wendys", price=2000)
restaurant4 = Restaurant(name="Subway", price=5000)
restaurant5 = Restaurant(name="Taco Bell", price=4000)

review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=5)
review2 = Review(customer=customer2, restaurant=restaurant2, star_rating=9)
review3 = Review(customer=customer3, restaurant=restaurant3, star_rating=7)
review4 = Review(customer=customer4, restaurant=restaurant4, star_rating=6)
review5 = Review(customer=customer5, restaurant=restaurant5, star_rating=8)


session.add_all([customer1, customer2, customer3, customer4, customer5])
session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5])
session.add_all([review1, review2, review3, review4, review5])

session.commit()