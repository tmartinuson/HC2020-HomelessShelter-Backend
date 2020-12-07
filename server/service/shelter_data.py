from .base import Base
from ..model.shelter import Shelter


class ShelterAlreadyExistsError(Exception):
    pass


class ShelterNotFoundError(Exception):
    pass


class ShelterData(Base):

    def create(self, name, address_line_1, address_line_2, num_beds,
               coordinate_x, coordinate_y, post_code, phone, email):
        shelter = self.session.query(Shelter).filter(
            Shelter.name == name).first()
        if shelter:
            raise ShelterAlreadyExistsError()

        shelter = Shelter()
        shelter.name = name
        shelter.address_line_1 = address_line_1
        shelter.address_line_2 = address_line_2
        shelter.num_beds = num_beds
        shelter.coordinate_x = coordinate_x
        shelter.coordinate_y = coordinate_y
        shelter.post_code = post_code
        shelter.phone = phone
        shelter.email = email

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
