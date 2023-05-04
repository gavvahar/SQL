from imports import *
from classes import *
from db import *


def assign_team(hero_name, team_name):
    with Session(engine) as session:
        statement1 = (
            select(Hero, Team)
            .where(Team.name == team_name)
            .where(Hero.name == hero_name)
        )
        results1 = session.exec(statement1)
        for hero, team in results1:
            team.add_heroes.append(hero)
            session.add(team)
            session.commit()
            session.refresh(hero)
            print(f"{team.name} new hero:", hero)
