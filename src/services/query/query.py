from src.config.schemas.query import Query


class QueryService():

    def __init__(self, db) -> None:
        self.db = db

    def get_queries(self):
        result = self.db.query(Query).all()
        return result