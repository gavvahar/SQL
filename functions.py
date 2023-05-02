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
    with Session(engine) as session:
        for x in hero:
            session.add(x)
        session.commit()
        session.close()


def main():
    create_db_and_tables()
    create_heros()
