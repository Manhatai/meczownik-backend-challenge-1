from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.database.database_connection import Base


class CountryModel(Base):
    __tablename__ = 'country'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    stadium: Mapped[list["StadiumModel"]] = relationship("StadiumModel", back_populates="country")
    team: Mapped[list["TeamModel"]] = relationship("TeamModel", back_populates="country")