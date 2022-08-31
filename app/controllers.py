import databases as databases
from fastapi import FastAPI, Response, Request, Cookie, Depends
from crud import *

from models import SQLALCHEMY_DATABASE_URL, SessionLocal, User


database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@app.get("/")
async def root(request: Request, response: Response, db=Depends(get_db)):
    request = request
    response = response
    user = db.query(User)


    return {"message": "Hello World"}
