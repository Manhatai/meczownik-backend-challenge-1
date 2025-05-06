from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.database.database_connection import get_db
from infra.database.database_queries import (query_single_item, query_multiple_items)
from infra.models import StadiumModel
from infra.schemas.stadium_schema import StadiumSchema

stadium_router = APIRouter()

@stadium_router.get("/stadium", response_model=list[StadiumSchema], status_code=200)
async def get_all_buildings(db: Session = Depends(get_db)) -> list[type[StadiumModel]]:
    return query_multiple_items(db, StadiumModel)

@stadium_router.get("/stadium/{stadium_id}", response_model=StadiumSchema, status_code=200)
async def get_single_building(stadium_id: int, db: Session = Depends(get_db)) -> type[StadiumModel]:
    return query_single_item(db, StadiumModel, stadium_id, 'Stadium')