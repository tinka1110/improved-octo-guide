import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

PORT = 5000

# Example room
rooms = [
    {"room_number": 101, "room_type": "Single", "price": 100},
    {"room_number": 102, "room_type": "Double", "price": 150},
    {"room_number": 103, "room_type": "Suite", "price": 200},
]

#api
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# api
@app.get("/")
def hello():
    return { "message": "Hello FastAPI" }

# /rooms
@app.get("/rooms")
async def get_rooms():
    return rooms

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",
        ssl_certfile="/etc/letsencrypt/fullchain.pem",
    )
