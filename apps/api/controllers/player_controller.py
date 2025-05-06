from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.database.database_connection import get_db
from infra.database.database_queries import (query_single_item, query_multiple_items)
from infra.models import PlayerModel
from infra.schemas.player_schema import PlayerSchema

player_router = APIRouter()

@player_router.get("/player", response_model=list[PlayerSchema], status_code=200)
async def get_all_buildings(db: Session = Depends(get_db)) -> list[type[PlayerModel]]:
    return query_multiple_items(db, PlayerModel)

@player_router.get("/player/{player_id}", response_model=PlayerSchema, status_code=200)
async def get_single_building(player_id: int, db: Session = Depends(get_db)) -> type[PlayerModel]:
    return query_single_item(db, PlayerModel, player_id, 'Player')