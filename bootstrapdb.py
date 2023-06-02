from faker import Faker

from models import Base, Film, FilmActor, FilmCategory, Category, Rental, Payment, Staff, City, Country, Store, \
    Language, Inventory, Actor, Customer, Address
from session import session


def generate_category(session, count=50):
    fake = Faker()
    session.add_all([
        Category(
            id=fake.id(),
            name=fake.name(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_film_category(session, count=50):
    fake = Faker()
    for film_category in session.query(FilmCategory):
        film_category.category.extend([
            FilmCategory(
                id=fake.id(),
                name=fake.name(),
                last_update=fake.last_update()
            )
        ])
    session.commit()


def generate_film(session, count=10):
    fake = Faker()
    session.add_all([
        Film(
            id=fake.id(),
            title=fake.title(),
            description=fake.text(),
            release_date=fake.date(),
            language_id=fake.language_id(),
            rental_duration=fake.random_int(min=1, max=12),
            rental_rate=fake.random_int(min=1, max=100),
            length=fake.random_int(min=1, max=100),
            replacement_cost=fake.random_int(min=1, max=100),
            rating=fake.random_int(min=1, max=100),
            special_features=fake.text(),
            last_update=fake.last_update(),
            fulltext=fake.text()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_language(session, count=10):
    fake = Faker()
    session.add_all([
        Language(
            language_id=fake.language_id(),
            name=fake.name(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_inventory(session, count=10):
    fake = Faker()
    session.add_all([
        Inventory(
            inventory_id=fake.inventory_id(),
            film_id=fake.id(),
            store_id=fake.id(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_rental(session, count=10):
    fake = Faker()
    session.add_all([
        Rental(
            rental_id=fake.rental_id(),
            rental_date=fake.date(),
            customer_id=fake.id(),
            inventory_id=fake.id(),
            return_date=fake.date(),
            stuff_id=fake.id(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_film_actor(session, count=10):
    fake = Faker()
    session.add_all([
        FilmActor(
            film_id=fake.id(),
            actor_id=fake.id(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_actor(session, count=10):
    fake = Faker()
    session.add_all([
        Actor(
            actor_id=fake.id(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_customer(session, count=10):
    fake = Faker()
    session.add_all([
        Customer(
            customer_id=fake.id(),
            store_id=fake.id(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            address_id=fake.address_id(),
            acitive_is=fake.active_is(),
            create_date=fake.date(),
            last_update=fake.last_update(),
            rental_id=fake.random_int(min=1, max=100)
        )
        for _ in range(count)
    ])
    session.commit()


def generate_payment(session, count=10):
    fake = Faker()
    session.add_all([
        Payment(
            payment_id=fake.id(),
            rental_id=fake.id(),
            staff_id=fake.id(),
            amount=fake.random_int(min=1, max=100),
            payment_date=fake.payment_date(),
            customer_id=fake.id(),
        )
        for _ in range(count)
    ])
    session.commit()


def generate_address(session, count=10):
    fake = Faker()
    session.add_all([
        Address(
            address_id=fake.id(),
            address=fake.address(),
            address2=fake.address2(),
            district=fake.district(),
            city_id=fake.city_id(),
            postal_code=fake.postal_code(),
            phone=fake.phone_number(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_staff(session, count=10):
    fake = Faker()
    session.add_all([
        Staff(
            staff_id=fake.id(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address_id=fake.address_id(),
            active=fake.active,
            store_id=fake.id(),
            username=fake.username(),
            password=fake.password(),
            last_update=fake.last_update(),
            picture=fake.image_url()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_city(session, count=10):
    fake = Faker()
    session.add_all([
        City(
            city_id=fake.id(),
            city=fake.city(),
            country_id=fake.country_id(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_country(session, count=10):
    fake = Faker()
    session.add_all([
        Country(
            country_id=fake.id(),
            country=fake.country(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_store(session, count=10):
    fake = Faker()
    session.add_all([
        Store(
            store_id=fake.id(),
            manager_staff_id=fake.id(),
            address_id=fake.address_id(),
            last_update=fake.last_update()
        )
        for _ in range(count)
    ])
    session.commit()


def main():
    Base.metadata.create_all()

    generate_film(session)
    generate_category(session)
    generate_film_category(session)
    generate_language(session)
    generate_inventory(session)
    generate_rental(session)
    generate_film_actor(session)
    generate_actor(session)
    generate_customer(session)
    generate_payment(session)
    generate_address(session)
    generate_staff(session)
    generate_city(session)
    generate_country(session)
    generate_store(session)


if __name__ == '__main__':
    main()
