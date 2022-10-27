import uvicorn
from fastapi import FastAPI
from datetime import datetime
from pydantic.main import BaseModel
from pydantic import BaseModel, Field
from typing import Dict, List, Optional

app = FastAPI()

from config.routes import setup_routes

setup_routes(app)

@app.get("/health/", tags=["health"])
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
