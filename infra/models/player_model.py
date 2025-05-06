from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.database.database_connection import Base


class PlayerModel(Base):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"), nullable=False)
    team: Mapped["TeamModel"] = relationship("TeamModel", back_populates="player")
    squad_number: Mapped[str] = mapped_column(String, nullable=False)