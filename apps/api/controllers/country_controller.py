from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.database.database_connection import get_db
from infra.database.database_queries import (query_single_item, query_multiple_items)
from infra.models.country_model import CountryModel
from infra.schemas.country_schema import CountrySchema

country_router = APIRouter()

@country_router.get("/country", response_model=list[CountrySchema], status_code=200)
async def get_all_buildings(db: Session = Depends(get_db)) -> list[type[CountryModel]]:
    return query_multiple_items(db, CountryModel)

@country_router.get("/country/{country_id}", response_model=CountrySchema, status_code=200)
async def get_single_building(country_id: int, db: Session = Depends(get_db)) -> type[CountryModel]:
    return query_single_item(db, CountryModel, country_id, 'Country')