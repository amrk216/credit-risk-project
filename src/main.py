from fastapi import FastAPI,APIRouter
from dotenv import load_dotenv
load_dotenv(".env")
from routers import base,data,predict  

app = FastAPI()
 
app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(predict.predict_router)