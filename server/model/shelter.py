from sqlalchemy import String, Integer, Column, Float

from .base import Base


class Shelter(Base):
    __tablename__ = 'shelters'

    name = Column(String(256), primary_key=True)
    num_beds = Column(Integer, nullable=False)
    coordinate_x = Column(Float, nullable=False)
    coordinate_y = Column(Float, nullable=False)
    address_line_1 = Column(String(256), nullable=False)
    address_line_2 = Column(String(256), nullable=False)
    post_code = Column(String(256), nullable=False)
    phone = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)

    def __repr__(self):
        return f'<Shelter name={self.name} num_beds={self.num_beds} ' \
               f'coordinate_x={self.coordinate_x} coordinate_y={self.coordinate_y}' \
               f'address_line_1={self.address_line_1} address_line_2={self.address_line_2}' \
               f'post_code={self.post_code} phone={self.phone} email={self.email}>'

    def to_string(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(self.name, self.address_line_1, self.address_line_2,
                                                            self.coordinate_x, self.coordinate_y,
                                                            self.num_beds, self.post_code, self.phone, self.email)

    def to_dict(self):
        return {
            'name': self.name,
            'address_line_1': self.address_line_1,
            'address_line_2': self.address_line_2,
            'num_beds': self.num_beds,
            'coordinate_x': self.coordinate_x,
            'coordinate_y': self.coordinate_y,
            'post_code': self.post_code,
            'phone': self.phone,
            'email': self.email
        }
