from imports import *
from classes import *
from db import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        teams = [
            Team(name="Preventers", headquarters="Sharp Tower"),
            Team(name="Z-Force", headquarters="Sister Margaret's Bar"),
        ]
        for t in teams:
            session.add(t)
        session.commit()
        heroes = [
            Hero(name="Deadpond", secret_name="Dive Wilson", team_id=teams[1].id),
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
            Hero(
                name="Rust-Man", secret_name="Tommy Sharp", age=48, team_id=teams[0].id
            ),
            Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
            Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
            Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
            Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93),
        ]

        for x in heroes:
            session.add(x)
            session.commit()
            session.refresh(x)
            print("Created hero:", x)
            
        
        def add_team(hero_name, team_name):
            statement = select(Hero.id, Team.id).where(Hero.name == hero_name).where(Team.name == team_name)
            results = session.exec(statement)
            for hero, team in results:
                heroes[hero-1].team_id = team
                session.add(heroes[hero-1])
                session.commit()
                session.refresh(heroes[hero-1])
                print("Updated hero:", heroes[hero-1])
        
        add_team("Spider-Boy", "Preventers")
        
        def delete_team(hero_id):
            old_team = heroes[hero_id].team_id-1
            heroes[hero_id].team_id = None
            session.add(heroes[hero_id])
            session.commit()
            session.refresh(heroes[hero_id])
            print(f"No longer {teams[old_team].name}:", heroes[hero_id])
        
        delete_team(1)


def select_heroes(team_name):
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team).where(Team.name == team_name)
        results = session.exec(statement)
        for hero, team in results:
            print(f"{team_name} Hero:", hero, "Team:", team)


def main():
    create_db_and_tables()
    create_heroes()
    select_heroes("Preventers")