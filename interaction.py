
import os
from datetime import date
import random
from model import Hero, Moto, History, Fight
import logg
from sqlalchemy import delete, create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv 


load_dotenv()
engine = create_engine(os.environ.get('DATABASE_URL_LOCAL'))
Session = sessionmaker(bind=engine)

logger = logg.get_logger('logger')

def get_id_from_hero_name(name):
    with Session() as session:
        id = session.query(Hero.id).filter(Hero.name==name).limit(1)
    return id

def add_hero(name, side, birthday):
    birthday=date.fromisoformat(birthday)
    with Session() as session:
        session.add(Hero(name=name, side=side, birthday=birthday))
        session.commit()
    logger.info(f"Hero {name} added")

def add_moto(name, moto):
    hero_id = get_id_from_hero_name(name)
    with Session() as session:
        if not session.query(hero_id.exists()).scalar():
            logger.error("This hero has not been added")
        else:
                moto_id = session.query(Moto).filter(Moto.hero_id==hero_id).count() + 1
                session.add(Moto(hero_id=hero_id, moto_id=moto_id, moto=moto))
                session.commit()
                logger.info(f"Moto #{moto_id} for hero {name} added")

def add_fight():
    with Session() as session:
        random_hero_1_id = random.choice([hero.id for hero in session.query(Hero).filter(Hero.side=='Шиноби')])
        try:
            random_hero_1_moto_id = random.choice([moto.id for moto in session.query(Moto).filter(Moto.hero_id==random_hero_1_id)])
        except:
            random_hero_1_moto_id = None    
        random_hero_2_id = random.choice([hero.id for hero in session.query(Hero).filter(Hero.side=='Акацуки')])
        try:
            random_hero_2_moto_id = random.choice([moto.id for moto in session.query(Moto).filter(Moto.hero_id==random_hero_2_id)])
        except:
            random_hero_2_moto_id = None
        random_winner = random.choice([0, 1, 2])

        session.add(Fight(
            hero_1_id=random_hero_1_id,
            hero_1_moto_id=random_hero_1_moto_id,
            hero_2_id=random_hero_2_id,
            hero_2_moto_id=random_hero_2_moto_id,
            winner=random_winner
        ))
        session.commit()
    logger.info(f"Fight between {random_hero_1_id} and {random_hero_2_id} added with winner {random_winner}")

def add_story(name, story):
    hero_id = get_id_from_hero_name(name)
    with Session() as session:
        if not session.query(hero_id.exists()).scalar():
            logger.error("This hero has not been added")
        else:
            session.add(History(hero_id=hero_id, story=story))
            session.commit()
            logger.info(f"Story for hero {name} added")

def delete_hero(name):
    hero_id = get_id_from_hero_name(name)
    with Session() as session:
        if not session.query(hero_id.exists()).scalar():
            logger.error("This hero has not been added")
        else:
            session.execute(delete(Hero).where(Hero.name==name))
            session.commit()
            logger.info(f"Hero {name} deleted")
