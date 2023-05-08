from edit_team import *


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
            Hero(name="Princess Sure-E", secret_name="Sure-E"),
        ]
        team_link = [
            HeroTeamLink(team=teams[1], hero=heroes[0]),
            HeroTeamLink(team=teams[0], hero=heroes[0], is_training=True),
            HeroTeamLink(team=teams[0], hero=heroes[2]),
            HeroTeamLink(team=teams[0], hero=heroes[1], is_training=True),
        ]

        for x in team_link:
            session.add(x)
            session.commit()
            # session.refresh(x)
            # print(f"{x.name}:", x.name)
            # print(f"{x.name} Teams:", x.team)


def select_heroes(team_name: str):
    with Session(engine) as session:
        statement = select(Team).where(Team.name == team_name)
        results = session.exec(statement)
        for team in results:
            print(f"{team_name} heroes:", team.add_heroes)


def main():
    create_db_and_tables()
    create_heroes()
    # assign_team("Tarantula", "Preventers")
    # assign_team("Dr. Weird", "Preventers")
    # assign_team("Captain North America", "Preventers")
    # select_heroes("Preventers")
    # delete_team("Spider-Boy")
    update_heroes("Spider-Boy", "Z-Force", True, "Preventers")
