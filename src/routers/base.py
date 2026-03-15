from fastapi import APIRouter, Depends
from helpers.config import Settings, get_settings
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["base"]
)

@base_router.get("/")
async def Health(app_settings: Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {"app_name": app_name,
            "version": app_version
            }


@base_router.get("/MODEL_INFO")
async def ModelInfo(app_settings: Settings = Depends(get_settings)):
    name_model = app_settings.NAME_MODEL
    version_model = app_settings.VERSION_MODEL
    roc_auc = app_settings.ROC_AUC
    return {"model_name": name_model,
            "model_version": version_model,
            "roc_auc": roc_auc
            }

