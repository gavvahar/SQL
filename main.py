from project.db import *
from project.classes import Hero


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/")
def create_heroes(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


# def create_heroes(hero: Hero):
#     with Session(engine) as session:
#         heroes = [
#             Hero(name="Deadpond", secret_name="Dive Wilson"),
#             Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
#             Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48),
#             Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
#             Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
#             Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
#             Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93),
#             Hero(name="Princess Sure-E", secret_name="Sure-E"),
#         ]

#         for x in heroes:
#             session.add(x)
#             session.commit()


@app.get("/heroes/")
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes
