import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from base import Base
from base import session
from review import Review
from sqlalchemy.orm import relationship
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Restaurant", secondary="review", back_populates="customers")

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max(self.reviews, key=lambda r: r.star_rating).restaurant

    def add_review(self, restaurant, rating):
        new_review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant.id).delete()
        session.commit()