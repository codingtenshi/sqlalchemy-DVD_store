from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    last_update = Column(String(50))

    def __repr__(self):
        return f'Category {self.name}'


class FilmCategory(Base):
    __tablename__ = 'film_category'
    film_id = Column(Integer, primary_key=True)
    category_id = Column(Integer, primary_key=True)
    last_update = Column(String(50))

    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')
    category = relationship('Category', cascade='all, delete, delete-orphan')
    film = relationship('Film', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'FilmCategory {self.film_id} {self.category_id}'


class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    language_id = Column(Integer, nullable=False)
    rental_duration = Column(Integer, nullable=False)
    rental_rate = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    replacement_cost = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    last_update = Column(String(50))
    special_features = Column(String(50))
    fulltext = Column(String(50))

    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Film {self.title}'


class Language(Base):
    __tablename__ = 'language'
    lang_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_update = Column(String(50))

    film = relationship('Film', cascade='all, delete, delete-orphan')
    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')
    actor = relationship('Actor', cascade='all, delete, delete-orphan')
    category = relationship('Category', cascade='all, delete, delete-orphan')
    film_text = relationship('FilmText', cascade='all, delete, delete-orphan')
    film_actor = relationship('FilmActor', cascade='all, delete, delete-orphan')
    country = relationship('Country', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    store = relationship('Store', cascade='all, delete, delete-orphan')
    address = relationship('Address', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Language {self.name}'


class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, primary_key=True)
    last_update = Column(String(50))

    film_actor = relationship('FilmActor', cascade='all, delete, delete-orphan')
    film = relationship('Film', cascade='all, delete, delete-orphan')
    actor = relationship('Actor', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'FilmActor {self.actor_id} {self.film_id}'


class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    last_update = Column(String(50))

    film_actor = relationship('FilmActor', cascade='all, delete, delete-orphan')
    film = relationship('Film', cascade='all, delete, delete-orphan')
    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')
    category = relationship('Category', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    store = relationship('Store', cascade='all, delete, delete-orphan')
    address = relationship('Address', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Actor {self.first_name} {self.last_name}'


class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, nullable=False)
    store_id = Column(Integer, nullable=False)
    last_update = Column(String(50))

    film = relationship('Film', cascade='all, delete, delete-orphan')
    store = relationship('Store', cascade='all, delete, delete-orphan')
    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')
    category = relationship('Category', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    address = relationship('Address', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Inventory {self.film_id} {self.store_id}'


class Rental(Base):
    __tablename__ = 'rental'
    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    rental_date = Column(String(50), nullable=False)
    inventory_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    return_date = Column(String(50))
    staff_id = Column(Integer, nullable=False)
    last_update = Column(String(50))

    rental = relationship('Rental', cascade='all, delete, delete-orphan')
    inventory = relationship('Inventory', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    address = relationship('Address', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Rental {self.rental_id} {self.rental_date} {self.inventory_id} {self.customer_id} {self.return_date}'


class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    address_id = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    create_date = Column(String(50))
    last_update = Column(String(50))
    rental_id = Column(Integer, nullable=False)

    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    store = relationship('Store', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Customer {self.customer_id} {self.store_id} {self.first_name} {self.last_name} {self.email}'


class Payment(Base):
    __tablename__ = 'payment'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False)
    staff_id = Column(Integer, nullable=False)
    rental_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    payment_date = Column(String(50), nullable=False)

    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    rental = relationship('Rental', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Payment {self.payment_id} {self.customer_id} {self.staff_id} {self.rental_id} {self.amount} '


class Address(Base):
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(50), nullable=False)
    address2 = Column(String(50), nullable=False)
    city_id = Column(Integer, nullable=False)
    postal_code = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    last_update = Column(String(50))

    def __repr__(self):
        return f'Address {self.address_id} {self.address} {self.address2} {self.postal_code} {self.phone} '


class Store(Base):
    __tablename__ = 'store'
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    manager_staff_id = Column(Integer, nullable=False)
    address_id = Column(Integer, nullable=False)
    last_update = Column(String(50))

    manager_staff = relationship('Staff', cascade='all, delete, delete-orphan')
    address = relationship('Address', cascade='all, delete, delete-orphan')
    rental = relationship('Rental', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    film = relationship('Film', cascade='all, delete, delete-orphan')
    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')
    film_actor = relationship('FilmActor', cascade='all, delete, delete-orphan')
    category = relationship('Category', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Store {self.store_id} {self.manager_staff_id} {self.address_id}'


class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_id = Column(Integer, nullable=False)
    store_id = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    last_update = Column(String(50))
    picture = Column(String(50))

    staff = relationship('Staff', cascade='all, delete, delete-orphan')
    address = relationship('Address', cascade='all, delete, delete-orphan')
    store = relationship('Store', cascade='all, delete, delete-orphan')
    rental = relationship('Rental', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    film = relationship('Film', cascade='all, delete, delete-orphan')
    film_category = relationship('FilmCategory', cascade='all, delete, delete-orphan')
    film_actor = relationship('FilmActor', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Staff {self.staff_id} {self.first_name} {self.last_name} {self.active} {self.username}'


class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country_id = Column(Integer, nullable=False)
    last_update = Column(String(50))

    country = relationship('Country', cascade='all, delete, delete-orphan')
    store = relationship('Store', cascade='all, delete, delete-orphan')
    rental = relationship('Rental', cascade='all, delete, delete-orphan')
    customer = relationship('Customer', cascade='all, delete, delete-orphan')
    film = relationship('Film', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'City {self.city_id} {self.city} {self.country_id} {self.last_update}'


class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(50), nullable=False)
    last_update = Column(String(50))

    store = relationship('Store', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'Country {self.country_id} {self.country} {self.last_update}'

