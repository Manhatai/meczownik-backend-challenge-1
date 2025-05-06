from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.database.database_connection import Base


class MatchModel(Base):
    __tablename__ = 'match'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    team1_id: Mapped[int] = mapped_column(ForeignKey("team.id"), nullable=False)
    team1: Mapped["TeamModel"] = relationship("TeamModel", foreign_keys=[team1_id], back_populates="team1_matches")
    team2_id: Mapped[int] = mapped_column(ForeignKey("team.id"), nullable=False)
    team2: Mapped["TeamModel"] = relationship("TeamModel", foreign_keys=[team2_id], back_populates="team2_matches")
    team1_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    team2_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    winner_id: Mapped[int] = mapped_column(ForeignKey("team.id"), default=None)
    winner: Mapped["TeamModel"] = relationship("TeamModel", foreign_keys=[winner_id], back_populates="won_matches")
    stadium_id: Mapped[int] = mapped_column(ForeignKey("stadium.id"), nullable=False)
    stadium: Mapped["StadiumModel"] = relationship("StadiumModel", back_populates="match")
    date_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    date_end: Mapped[DateTime] = mapped_column(DateTime, default=None)
    status: Mapped[str] = mapped_column(String, nullable=False)