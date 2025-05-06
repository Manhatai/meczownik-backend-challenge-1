from typing import Optional

from pydantic import BaseModel
from infra.schemas.team_schema import TeamSchema


class PlayerSchema(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    team_id: int
    team: Optional[TeamSchema] = None
    squad_number: int
