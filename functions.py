from edit_team import *


def create_heroes():
    with Session(engine) as session:
        teams = [
            Team(name="Preventers", headquarters="Sharp Tower"),
            Team(name="Z-Force", headquarters="Sister Margaret's Bar"),
        ]
        heroes = [
            Hero(name="Deadpond", secret_name="Dive Wilson", team=[teams[1], teams[0]]),
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador", team=[teams[0]]),
            Hero(name="Rust-Man", secret_name="Tommy Sharp", age=48, team=[teams[0]]),
            Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32),
            Hero(name="Black Lion", secret_name="Trevor Challa", age=35),
            Hero(name="Dr. Weird", secret_name="Steve Weird", age=36),
            Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93),
            Hero(name="Princess Sure-E", secret_name="Sure-E"),
        ]

        for x in heroes:
            session.add(x)
            session.commit()
            session.refresh(x)
            print(f"{x.name}:", x.name)
            print(f"{x.name} Teams:", x.team)

        teams.append(
            Team(
                name="Wakaland",
                headquarters="Wakaland Capital City",
                add_heroes=[heroes[4], heroes[7]],
            )
        )
        for x1 in teams:
            session.add(x1)
            session.commit()
            session.refresh(x1)


def select_heroes(team_name):
    with Session(engine) as session:
        statement = select(Team).where(Team.name == team_name)
        results = session.exec(statement)
        for team in results:
            print(f"{team_name} heroes:", team.add_heroes)


def main():
    create_db_and_tables()
    create_heroes()
    assign_team("Tarantula", "Preventers")
    assign_team("Dr. Weird", "Preventers")
    assign_team("Captain North America", "Preventers")
    select_heroes("Preventers")
    delete_team("Spider-Boy")
    update_heroes("Spider-Boy", "Z-Force")
