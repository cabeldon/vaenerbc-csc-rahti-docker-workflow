from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
app = FastAPI()

origins = [
    "*"
]
rooms = [
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/rooms")
def get_rooms():
    return rooms

@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host }


@app.get("/ip, response_class=HTMLResponse")
def ip(request: Request):
    return f"<h1>Din ip här {request.client.host}</h1>"

@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

