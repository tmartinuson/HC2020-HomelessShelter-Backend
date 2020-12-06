from sqlalchemy import String, Integer, Column

from .base import Base


class Shelter(Base):
    __tablename__ = 'shelters'

    name = Column(String(256), primary_key=True)
    num_beds = Column(Integer, nullable=False)
    location = Column(String(256), nullable=False)          # Address location
    coordinates = Column([float, float], nullable=False)    # Coordinates for API stored in float

    def __repr__(self):
        return f'<Shelter name={self.name} num_beds={self.num_beds} ' \
               f'location={self.location} coordinates={self.coordinates}>'
