from imports import *
from classes import *
from db import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
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


def update_heroes(name):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == name)
        results = session.exec(statement)
        hero = results.one()

        if name == "Spider-Boy":
            hero.age = 16
            hero.name = "Spider_Youngster"
        if name == "Captain North America":
            hero.name = "Captain North America Except Canada"
            hero.age = 110
        session.add(hero)

        session.commit()
        session.refresh(hero)


def main():
    create_db_and_tables()
    create_heroes()
    update_heroes("Spider-Boy")
    update_heroes("Captain North America")
