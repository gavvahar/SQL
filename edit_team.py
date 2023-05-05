from classes import *
from db import *


def assign_team(hero_name, team_name):
    with Session(engine) as session:
        statement = (
            select(Hero, Team)
            .where(Team.name == team_name)
            .where(Hero.name == hero_name)
        )
        results = session.exec(statement)
        for hero, team in results:
            team.add_heroes.append(hero)
            session.add(team)
            session.commit()
            session.refresh(hero)
            print(f"{team.name} new hero:", hero)


def delete_team(hero_name):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == hero_name)
        results = session.exec(statement)
        for hero in results:
            hero.team.clear()
            session.add(hero)
            session.commit()
            session.refresh(hero)
            print(f"{hero.name} without a team:", hero)


def update_heroes(hero_name, team_name):
    with Session(engine) as session:
        hero = session.exec(select(Hero).where(Hero.name == hero_name)).one()
        team = session.exec(select(Team).where(Team.name == team_name)).one()
        team.add_heroes.append(hero)
        session.add(team)
        session.commit()

        print(f"Updated {hero_name}'s Teams:", hero.team)
        print(f"{team.name} heroes:", team.add_heroes)

        hero.team.remove(team)
        session.add(team)
        session.commit()

        print(f"Reverted {team_name}'s heroes:", team.add_heroes)
        print(f"Reverted {hero_name}'s teams:", hero.team)
