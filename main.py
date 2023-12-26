import uvicorn
from fastapi import FastAPI

from routers import user, auth, item
from config import *


app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(item.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
