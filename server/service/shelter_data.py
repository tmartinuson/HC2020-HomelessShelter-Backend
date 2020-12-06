from .base import Base
from ..model.shelter import Shelter


class ShelterAlreadyExistsError(Exception):
    pass


class AccountNotFoundError(Exception):
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
            raise AccountNotFoundError()
        
        shelter = self.session.query(Shelter).filter(Shelter.name == name).first()
        return shelter
