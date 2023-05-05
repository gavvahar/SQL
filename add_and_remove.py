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
            hero.team_id = None
            session.add(hero)
            session.commit()
            session.refresh(hero)
            print(f"{hero.name} without a team:", hero)
