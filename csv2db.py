import csv
import os
from pprint import pprint as pp

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import or_

sqlite = 'sqlite:///sql.db'
#sqlite = 'sqlite://

Base = declarative_base()

class License(Base):
    # this is comment
    __tablename__ = 'licenses'

    id = Column(Integer, primary_key=True)
    """ Primary key """
    name = Column(String(255))
    """ License holders name """
    address = Column(String(255))
    postcode = Column(String(255))
    city = Column(String(255))
    license_granting_date = Column(String(255))
    license_type = Column(String(255))
    business_id = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        """ String representation of the object"""
        return "<License (name='%s', created_at='%s')>" % (self.name, self.created_at)

db = create_engine(sqlite)
Session = sessionmaker(bind=db)

def insert2db(name, address, postcode, city, date, type, businessid):
    new_row = License(name=name, address=address, postcode=postcode, city=city, license_granting_date=date, license_type=type, business_id=businessid)
    db = Session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id

#pp(insert2db('test','test','test','test','test','test','test'))

#this needs to be done only when first creating the db
#Base.metadata.create_all(db)