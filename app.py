from fastapi import FastAPI, Header, Path, Query
from schemas import ResponseModel
from datetime import datetime
from uvicorn import run

app = FastAPI()

@app.get("/user/{user_id}", response_model=ResponseModel)
async def get_user_info(
    user_id: int = Path(...),
    timestamp: str | None = Query(None),
    client_version: str = Header(...)
):
    
    if timestamp is None:
        timestamp = datetime.utcnow().isoformat()

    message = f"Hello, user {user_id}!"

    return {
        "user_id": user_id,
        "timestamp": timestamp,
        "client_version": client_version,
        "message": message
    }

if __name__ == "__main__":
    run(app)