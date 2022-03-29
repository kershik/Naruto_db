import argparse
import os
import logg
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import db, Hero
from dotenv import load_dotenv 

load_dotenv()

engine = create_engine(os.environ.get('DATABASE_URL'))
db.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

logger = logg.get_logger('logger')

parser = argparse.ArgumentParser()
parser.add_argument("--seed", help="full database",
                    action="store_true")
args = parser.parse_args()


if args.seed:
    with Session() as session:
        session.add(Hero(
            name='Наруто',
            side='Шиноби',
            birthday=date.fromisoformat('1001-12-04')
        ))
        logger.info("Hero Наруто added")
        session.add(Hero(
            name='Какаши',
            side='Шиноби',
            birthday=date.fromisoformat('0971-11-10')
        ))
        logger.info("Hero Какаши added")
        session.add(Hero(
            name='Шикамару',
            side='Шиноби',
            birthday=date.fromisoformat('1000-07-01')
        ))
        logger.info("Hero Шикамару added")
        session.add(Hero(
            name='Итачи',
            side='Акацуки',
            birthday=date.fromisoformat('0985-10-02')
        ))
        logger.info("Hero Итачи added")
        session.add(Hero(
            name='Дейдара',
            side='Акацуки',
            birthday=date.fromisoformat('0990-12-01')
        ))
        logger.info("Hero Дейдара added")
        session.add(Hero(
            name='Орочимару',
            side='Акацуки',
            birthday=date.fromisoformat('0950-03-12')
        ))
        logger.info("Hero Орочимару added")
        session.commit()
