from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host }


@app.get("/ip, response_class=HTMLResponse")
def ip(request: Request):
    return f"<h1>Din ip här {request.client.host}</h1>"

@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

