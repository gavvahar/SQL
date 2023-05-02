from typing import *
from sqlmodel import *


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heros():
    hero = [
        Hero(name="Deadpond", secret_name="Dive Wilson"),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
        Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48),
    ]
    session = Session(engine)
    for x in hero:
        session.add(x)
    session.commit()
    session.close()


def main():
    create_db_and_tables()
    create_heros()


if __name__ == "__main__":
    main()
