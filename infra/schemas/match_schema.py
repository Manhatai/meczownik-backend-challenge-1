from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from infra.schemas.stadium_schema import StadiumSchema
from infra.schemas.team_schema import TeamSchema


class MatchSchema(BaseModel):
    id: Optional[int] = None
    team1_id: int
    team1: Optional[TeamSchema] = None
    team2_id: int
    team2: Optional[TeamSchema] = None
    team1_goals: int
    team2_goals: int
    winner_id: int
    winner:Optional[TeamSchema] = None
    stadium_id: int
    stadium : Optional[StadiumSchema] = None
    date_start: datetime
    date_end: datetime
    status: str
