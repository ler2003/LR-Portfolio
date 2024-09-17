from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base_main_plate = declarative_base()

class Plate(Base_main_plate):
    __tablename__ = 'Plates'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    image = Column(String, nullable=False)
    url = Column(String, nullable=False)

    def toJSON(self):
        return {
            'id': self.id,
            'type': self.type,
            'image': self.image,
            'url': self.url
        }
