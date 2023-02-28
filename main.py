from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
  return {"Fuxi": "Contest"}


@app.get("/contests/{contest_id}")
async def read_contest(contest_id: int):
  return {"contest_id": contest_id}