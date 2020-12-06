from sqlalchemy import String, Column

from .base import Base


class Shelter(Base):
    __tablename__ = 'shelters'

    name = Column(String(256), primary_key=True)
    num_beds = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Shelter name={self.name} num_beds={self.num_beds}>'
