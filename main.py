from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root():
  return {"Fuxi": "Contest"}


@app.get("/contests/{id}", response_class=HTMLResponse)
async def read_contest(request: Request, id: str):
  return templates.TemplateResponse("contest.html", {"request": request, "id": id})