from imports import *
from classes import *
from db import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heros():
    hero = [
        Hero(name="Deadpond", secret_name="Dive Wilson"),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
        Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48),
    ]
    print("Before interacting with the database")
    for t in range(0, 3):
        print(f"Hero {t+1}:", hero[t])

    with Session(engine) as session:
        for x in hero:
            session.add(x)

        print("After adding to the session")
        for t in range(0, 3):
            print(f"Hero {t+1}:", hero[t])

        session.commit()

        print("After committing the session")
        for t in range(0, 3):
            print(f"Hero {t+1}:", hero[t])

            print("After committing the session, show IDs")
            for t in range(0, 3):
                print(f"Hero {t+1} ID:", hero[t].id)

            print("After committing the session, show names")
            for t in range(0, 3):
                print(f"Hero {t+1} name:", hero[t].name)

        for i in hero:
            session.refresh(i)

        print("After refreshing the heros")
        for t in range(0, 3):
            print(f"Hero {t+1}:", hero[t])

        print("After the session closes")
        for t in range(0, 3):
            print(f"Hero {t+1}:", hero[t])


def main():
    create_db_and_tables()
    create_heros()
