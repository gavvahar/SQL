from add_and_remove import *
from add_to_team import *


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        teams = [
            Team(name="Preventers", headquarters="Sharp Tower"),
            Team(name="Z-Force", headquarters="Sister Margaret's Bar"),
        ]
        heroes = [
            Hero(name="Deadpond", secret_name="Dive Wilson"),
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
            Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48),
            Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
            Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
            Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
            Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93),
            Hero(name="Princess Sure-E", secret_name="Sure-E")
        ]

        for x in heroes:
            session.add(x)
            session.commit()
            session.refresh(x)
            print("Created hero:", x)
            
        teams.append(Team(name="Wakaland", headquarters="Wakaland Capital City", add_heroes=[heroes[4], heroes[7]]))
        for x1 in teams:
            session.add(x1)
            session.commit()
            session.refresh(x1)
            
        assign_team("Deadpond", "Z-Force")
        assign_team("Rust-Man", "Preventers")
        
        add_team("Spider-Boy", "Preventers")
                
        


def select_heroes(team_name):
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team).where(Team.name == team_name)
        results = session.exec(statement)
        for hero, team1 in results:
            print(f"{team_name} Hero:", hero, "Team:", team1)


def main():
    create_db_and_tables()
    create_heroes()
    # select_heroes("Preventers")