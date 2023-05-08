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


def update_heroes(hero_name: str, team_name: str, traing=False, remove_team=""):
    with Session(engine) as session:
        hero = session.exec(select(Hero).where(Hero.name == hero_name)).one()
        team = session.exec(select(Team).where(Team.name == team_name)).one()

        team_link = HeroTeamLink(team=team, hero=hero, is_training=traing)
        team.hero_links.append(team_link)
        session.add(team)
        session.commit()

        print(f"Updated {hero.name}'s Teams:", hero.team_links)
        print(f"{team.name} heroes:", team.hero_links)

        for link in hero.team_links:
            if link.team.name == remove_team:
                link.is_training = False
            session.add(hero)
            session.commit()
            print(f"{hero_name} team: {link.team} is trinaing: {link.is_training}")
