from base import Base
from base import session
from sqlalchemy import Column, Integer, String, Float

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def reviews(self):
        return self.all_reviews()

    def customers(self):
        return self.customers

    @classmethod
    def fanciest(cls):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        review_strings = []
        for review in self.reviews:
            review_strings.append(f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars.")
        return review_strings

