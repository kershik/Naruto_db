import os
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


db = declarative_base()

class Hero(db):
    __tablename__ = 'hero'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    side = Column(String(30))
    birthday = Column(Date)
    moto = relationship('Moto', backref='hero', passive_deletes=True)
    history = relationship('History', uselist=False, backref='hero', passive_deletes=True)

    def __init__(self, name, side, birthday):
        self.name = name
        self.side = side
        self.birthday = birthday

    def __repr__(self):
        return f"{self.id} -> {self.name}"


class Moto(db):
    __tablename__ = 'moto'
    
    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('hero.id', ondelete='CASCADE'))
    moto_id = Column(Integer)
    moto = Column(String(100))
    
    def __init__(self, hero_id, moto_id, moto):
        self.hero_id = hero_id
        self.moto_id = moto_id
        self.moto = moto

    def __repr__(self):
        return f"{self.id} -> {self.hero_id} -> {self.moto}"

class Fight(db):
    __tablename__ = 'fight'
    
    id = Column(Integer, primary_key=True)
    hero_1_id = Column(Integer, ForeignKey("hero.id"), nullable=False)
    hero_1_id = Column(Integer, ForeignKey("hero.id"), nullable=False)
    hero_1_moto_id = Column(Integer, ForeignKey("moto.id"))
    hero_2_moto_id = Column(Integer, ForeignKey("moto.id"))
    winner = Column(Integer)
    
    def __init__(self, hero_1_id, hero_1_moto_id, hero_2_id, hero_2_moto_id, winner):
        self.hero_1_id = hero_1_id
        self.hero_2_id = hero_2_id
        self.hero_1_moto_id = hero_1_moto_id
        self.hero_2_moto_id = hero_2_moto_id
        self.winner = winner

    def __repr__(self):
        return f"{self.hero_1_id} + {self.hero_2_id} -> {self.winner}"

class History(db):
    __tablename__ = 'history'
    
    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('hero.id', ondelete='CASCADE'))
    story = Column(String)
    
    def __init__(self, hero_id, story):
        self.hero_id = hero_id
        self.story = story

    def __repr__(self):
        return f"{self.id} -> {self.hero_id} -> {self.story}"
