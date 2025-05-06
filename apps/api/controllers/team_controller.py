from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.database.database_connection import get_db
from infra.database.database_queries import (query_single_item, query_multiple_items)
from infra.models import TeamModel
from infra.schemas.team_schema import TeamSchema

team_router = APIRouter()

@team_router.get("/team", response_model=list[TeamSchema], status_code=200)
async def get_all_buildings(db: Session = Depends(get_db)) -> list[type[TeamModel]]:
    return query_multiple_items(db, TeamModel)

@team_router.get("/team/{team_id}", response_model=TeamSchema, status_code=200)
async def get_single_building(team_id: int, db: Session = Depends(get_db)) -> type[TeamModel]:
    return query_single_item(db, TeamModel, team_id, 'Team')