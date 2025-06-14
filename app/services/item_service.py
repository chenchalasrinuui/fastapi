from app.models.item_model import Item
from bson import ObjectId
from bson.errors import InvalidId

async def create_item_in_db(item: Item,db):
    result = await db["items"].insert_one(item.model_dump())
    return {"id": str(result.inserted_id), "item": item}

async def get_item_by_id(item_id: str,db):
    try:
        _id = ObjectId(item_id)
    except InvalidId:
        return None
    item = await db.items.find_one({"_id": ObjectId(item_id)}) # Convert str to ObjectId for query
    if item:
        item["_id"] = str(item["_id"]) # Convert ObjectId to string for serialization
        return item
    return {"message": "Item not found"}
