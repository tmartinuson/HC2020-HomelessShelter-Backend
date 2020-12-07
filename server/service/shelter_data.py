from .base import Base
from ..model.shelter import Shelter


class ShelterAlreadyExistsError(Exception):
    pass


class ShelterNotFoundError(Exception):
    pass


class ShelterData(Base):

    def create(self, name, address, num_beds, coordinate_x, coordinate_y):
        shelter = self.session.query(Shelter).filter(
            Shelter.name == name).first()
        if shelter:
            raise ShelterAlreadyExistsError()

        shelter = Shelter()
        shelter.name = name
        shelter.address = address
        shelter.num_beds = num_beds
        shelter.coordinate_x = coordinate_x
        shelter.coordinate_y = coordinate_y

        self.session.add(shelter)

    def get(self, name):
        shelter = self.session.query(Shelter).filter(
            Shelter.name == name).first()
        if not shelter:
            raise ShelterNotFoundError()
        
        shelter = self.session.query(Shelter).filter(Shelter.name == name).first()
        return shelter

    def update(self, name, num_beds):
        shelter = self.get(name)
        shelter.num_beds = num_beds

    def get_list(self):
        return self.session.query(Shelter).all()
