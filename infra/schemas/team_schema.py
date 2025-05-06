from typing import Optional

from pydantic import BaseModel
from infra.schemas.country_schema import CountrySchema

class TeamSchema(BaseModel):
    id: Optional[int] = None
    name: str
    trainer: str
    country_id: int
    country: Optional[CountrySchema] = None