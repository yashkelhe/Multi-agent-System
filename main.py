from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Order To Cash AI",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Order To Cash AI Running"
    }