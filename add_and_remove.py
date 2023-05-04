from imports import *
from classes import *
from db import *
def add_team(hero_name, team_name):
    with Session(engine) as session:
            statement = select(Hero, Team.id).where(Hero.name == hero_name).where(Team.name == team_name)
            results = session.exec(statement)
            for hero, team in results:
                hero.team_id = team
                session.add(hero)
                session.commit()
                session.refresh(hero)
                print("Updated hero:", hero)
        
        
        
# def delete_team(hero_id):
#     with Session(engine) as session:
#         old_team = heroes[hero_id].team_id-1
#         heroes[hero_id].team_id = None
#         session.add(heroes[hero_id])
#         session.commit()
#         session.refresh(heroes[hero_id])
#         print(f"No longer {teams[old_team].name}:", heroes[hero_id])
        
#         delete_team(1)