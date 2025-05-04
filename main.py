import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

PORT = 5000

# Exempelrum
rooms = [
    {"room_number": 101, "room_type": "Single", "price": 100},
    {"room_number": 102, "room_type": "Double", "price": 150},
    {"room_number": 103, "room_type": "Suite", "price": 200},
]


bookings = []

# Skapar FastAPI
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tillåter alla domäner
    allow_credentials=True,
    allow_methods=["*"],  # Tillåter alla HTTP-metoder
    allow_headers=["*"],  # Tillåter alla headers
)

# 
@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}

# GET /rooms 
@app.get("/rooms")
async def get_rooms():
    return rooms

# GET /bookings 
@app.get("/bookings")
async def get_bookings():
    return bookings

# POST /bookings 
@app.post("/bookings")
async def create_booking(request: Request):
    data = await request.json()

    
    if "room_number" not in data or "booking_date" not in data or "guest_name" not in data:
        return {"message": "Fel"}

    # Skapa bokningen
    new_booking = {
        "room_number": data["room_number"],
        "booking_date": data["booking_date"],
        "guest_name": data["guest_name"]
    }

    
    bookings.append(new_booking)

    return {"message": "Bokningen har sparats!"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",      
        ssl_certfile="/etc/letsencrypt/fullchain.pem",   
    )
