from imports import *
from classes import *
from db import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heros():
    heroes = [
        Hero(name="Deadpond", secret_name="Dive Wilson"),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
        Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48),
        Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
        Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
        Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
        Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93),
    ]

    with Session(engine) as session:
        for x in heroes:
            session.add(x)

        session.commit()


def select_heros():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        results = session.exec(statement)
        for hero in results:
            print(hero)


def main():
    create_db_and_tables()
    create_heros()
    select_heros()
