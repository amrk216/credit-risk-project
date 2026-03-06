from fastapi import FastAPI,APIRouter

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to the FastAPI application!"}