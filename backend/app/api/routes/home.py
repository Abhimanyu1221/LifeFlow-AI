from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session 

from app.db.session import get_db


router = APIRouter(
    prefix = "/api/v1",
    tags=["Home"],
)

@router.get("/")
def home():
    return{
        "message" : "Welcome to LifeFlow AI"
    }


@router.get("/database-test")
def database_test(
    db : Session = Depends(get_db),
):
    result = db.execute(text("SELECT 1"))

    return {
        "database" : result.scalar()
    }