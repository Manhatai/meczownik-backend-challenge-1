from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.database.database_connection import Base


class TeamModel(Base):
    __tablename__ = 'team'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    trainer: Mapped[str] = mapped_column(String, nullable=False)
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"), nullable=False)
    country: Mapped["CountryModel"] = relationship("CountryModel", back_populates="team")
    player: Mapped[list["PlayerModel"]] = relationship("PlayerModel", back_populates="team")
    team1_matches: Mapped[list["MatchModel"]] = relationship("MatchModel", foreign_keys="MatchModel.team1_id",
                                                             back_populates="team1")
    team2_matches: Mapped[list["MatchModel"]] = relationship("MatchModel", foreign_keys="MatchModel.team2_id",
                                                             back_populates="team2")
    won_matches: Mapped[list["MatchModel"]] = relationship("MatchModel", foreign_keys="MatchModel.winner_id",
                                                           back_populates="winner")
