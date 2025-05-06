from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.database.database_connection import get_db
from infra.database.database_queries import (query_single_item, query_multiple_items)
from infra.models import MatchModel
from infra.schemas.match_schema import MatchSchema

match_router = APIRouter()

@match_router.get("/match", response_model=list[MatchSchema], status_code=200)
async def get_all_buildings(db: Session = Depends(get_db)) -> list[type[MatchModel]]:
    return query_multiple_items(db, MatchModel)

@match_router.get("/match/{match_id}", response_model=MatchSchema, status_code=200)
async def get_single_building(match_id: int, db: Session = Depends(get_db)) -> type[MatchModel]:
    return query_single_item(db, MatchModel, match_id, 'Match')