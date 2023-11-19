from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.config.schemas.query import Query
from src.services.query.query import QueryService

from src.config import Session
from src.models.query.query import QueryModel


query_router=APIRouter()

# , response_model=List[QueryModel], status_code=200, dependencies=[Depends(JWTBearer())])
@query_router.get('/queries', tags=['queries'])
def get_queries() -> List[QueryModel]:
    db = Session()
    result = QueryService(db).get_queries()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@query_router.post('/queries', tags=['queries'])
def create_query(query: QueryModel) -> dict:
    db = Session()
    new_query = Query(**query.model_dump())
    db.add(new_query)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Query saved correctly"})