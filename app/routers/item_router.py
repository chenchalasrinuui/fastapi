from fastapi import APIRouter, HTTPException, Header
from app.models.item_model import Item
from app.services.item_service import create_item_in_db, get_item_by_id
from pydantic import BaseModel
from app.database.mongodb import get_db

router = APIRouter()
# Body model
class Data(BaseModel):
    rno: int
    age: int

@router.get("/test/{loc}")
async def test(loc: str,name: str):
    return {
        "message": f"Welcome {name} from {loc}!",
    }

@router.post("/test/{loc}")
async def test(loc: str,name: str, token: str = Header(),data: Data = None):
    return {
        "message": f"Welcome {name} from {loc}!",
        "token": token,
        "body": data
    }

@router.post("/save")
async def create_item(item: Item):
    return await create_item_in_db(item, get_db())

@router.get("/get/{item_id}")
async def get_item(item_id: str):
    item = await get_item_by_id(item_id,get_db())
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
