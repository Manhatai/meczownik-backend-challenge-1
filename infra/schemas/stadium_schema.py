from typing import Optional

from pydantic import BaseModel

from infra.schemas.country_schema import CountrySchema


class StadiumSchema(BaseModel):
    id: Optional[int] = None
    country_id: int
    country: Optional[CountrySchema] = None
    seats: int
    covered: bool