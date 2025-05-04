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

# bookings
bookings = [
    {"id": 1, "room_number": 101, "booking_date": "2025-05-01", "guest_name": "John Doe", "stars": None},
    {"id": 2, "room_number": 102, "booking_date": "2025-05-02", "guest_name": "Jane Smith", "stars": None},
]

# Skapar FastAPI
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


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
        "id": len(bookings) + 1,  
        "room_number": data["room_number"],
        "booking_date": data["booking_date"],
        "guest_name": data["guest_name"],
        "stars": None  # Startar utan stjärnor
    }

    bookings.append(new_booking)

    return {"message": "Bokningen har sparats!"}

# PUT /bookings/
@app.put("/bookings/{id}")
async def update_booking(id: int, stars: int):
    # Stjärnorna är mellan 1 och 5
    if stars < 1 or stars > 5:
        return {"message": "Stjärnorna måste bli mellan 1-5."}

    # Sök efter bokningen med det angivna ID:t
    for booking in bookings:
        if booking["id"] == id:
            booking["stars"] = stars  
            return {"message": "Recension uppdaterad"}
    
    return {"message": "Bokning inte hittad"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        ssl_keyfile="/etc/letsencrypt/privkey.pem",      
        ssl_certfile="/etc/letsencrypt/fullchain.pem",   
    )
