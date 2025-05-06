from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.database.database_connection import Base


class StadiumModel(Base):
    __tablename__ = 'stadium'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"), nullable=False)
    country: Mapped["CountryModel"] = relationship("CountryModel", back_populates="stadium")
    seats: Mapped[int] = mapped_column(Integer, nullable=False)
    covered: Mapped[int] = mapped_column(Boolean, nullable=False)
    match: Mapped[list["MatchModel"]] = relationship("MatchModel", back_populates="stadium")