import uvicorn
from fastapi import FastAPI
from users.router import router
from backend.database.database import create_tables

app = FastAPI()


@app.get("/")
async def root():
    return {"ok": True}


@app.post("/setup_db")
async def setup_db():
    await create_tables()
    return {"ok": True}


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="localhost", port=8000, reload=True)
