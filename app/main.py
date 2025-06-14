from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from app.routers import item_router
from app.database.mongodb import connect_to_mongo

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    await connect_to_mongo()  # This runs on startup
    yield                     # You can put shutdown logic after yield
    # Optional: close Mongo connection here

app = FastAPI(lifespan=lifespan)

app.include_router(item_router.router, prefix="/items", tags=["Items"])


