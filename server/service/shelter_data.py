from .base import Base
from ..model.shelter import Shelter


class ShelterData(Base):

    def create(self, name, address, num_beds, coordinate_x, coordinate_y):
        shelter = Shelter(name, num_beds, address, coordinate_x, coordinate_y)
        self.session.add(shelter)

    def get(self, name):
        shelter = self.session.query(Shelter).filter(Shelter.name == name).first()
        return shelter
