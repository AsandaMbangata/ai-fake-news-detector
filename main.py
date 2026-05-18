from fastapi import FastAPI

from api.user_api import router as user_router
from api.article_api import router as article_router
from api.result_api import router as result_router

app = FastAPI()

app.include_router(user_router)
app.include_router(article_router)
app.include_router(result_router)


@app.get("/")
def home():

    return {"message": "AI Fake News Detection API"}