from imports import *
from classes import *
from db import *


def add_team(hero_name, team_name):
    with Session(engine) as session:
        statement = (
            select(Hero, Team.id)
            .where(Hero.name == hero_name)
            .where(Team.name == team_name)
        )
        results = session.exec(statement)
        for hero, team in results:
            hero.team_id = team
            session.add(hero)
            session.commit()
            session.refresh(hero)
            print("Updated hero:", hero)


def delete_team(hero_name):
    with Session(engine) as session:
        statement = (
            select(Hero, Team)
            .where(Hero.name == hero_name)
            .where(Team.id == Hero.team_id)
        )
        results = session.exec(statement)
        for hero, team in results:
            old_team = team.name
            hero.team_id = None
            session.add(hero)
            session.commit()
            session.refresh(hero)
            print(f"No longer {old_team}:", hero)
