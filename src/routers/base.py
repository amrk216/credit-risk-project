from fastapi import APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["base"]
)

@base_router.get("/")
async def Health():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {"app_name": app_name,
            "version": app_version
            }


@base_router.get("/MODEL_INFO")
async def ModelInfo():
    name_model = os.getenv("NAME_MODEL")
    version_model = os.getenv("version_model")
    roc_auc = os.getenv("ROC_AUC")
    return {"model_name": name_model,
            "model_version": version_model,
            "roc_auc": roc_auc
            }

