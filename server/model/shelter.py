from sqlalchemy import String, Integer, Column, Float

from .base import Base


class Shelter(Base):
    __tablename__ = 'shelters'

    name = Column(String(256), primary_key=True)
    num_beds = Column(Integer, nullable=False)
    address = Column(String(256), nullable=False)           # Address location
    coordinate_x = Column(Float, nullable=False)            # Coordinate x for API stored in float
    coordinate_y = Column(Float, nullable=False)            # Coordinate y for API stored in float


    def __repr__(self):
        return f'<Shelter name={self.name} num_beds={self.num_beds} ' \
               f'location={self.location} coordinate_x={self.coordinate_x} coordinate_y={self.coordinate_y}>'

    def to_string(self):
        return '{0} {1} {2} {3} {4}'.format(self.name, self.address,
                                            self.coordinate_x, self.coordinate_y, self.num_beds)

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address,
            'coordinate_x': self.coordinate_x,
            'coordinate_y': self.coordinate_y,
            'num_beds': self.num_beds,
        }
