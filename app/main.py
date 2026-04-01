from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_conn

app = FastAPI()

origins = [
    "*"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Skapa databas-schema:
create_schema()

temp_rooms = [
    {  
        "room_number": 101,
        "beds" : 2, 
        "price": 600
    },
    {
        "room_number": 102, 
        "beds" : 1, 
        "price": 400
    },
    {
        "room_number": 103, 
        "beds" : 1, 
        "price": 400
    },
    {
        "room_number": 104, 
        "beds" : 2, 
        "price": 600
    }
]

@app.get("/")
def read_root():
    # testa databasen
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT 
                'databasen funkar!' AS msg, 
                version() AS version
        """)
        db_status = cur.fetchone()
    return { "msg": "Välkommen till hotellets boknings-API", "db": db_status}

@app.get("/rooms")
def rooms():
    return temp_rooms

@app.post("/bookings")
def create_bookings():
    # skapa bokning i databasen, INSERT INFO bookings...
    return {"msg": "Bokning skapad!"}




