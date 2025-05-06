from typing import Optional

from pydantic import BaseModel


class CountrySchema(BaseModel):
    id: Optional[int] = None
    name: str
