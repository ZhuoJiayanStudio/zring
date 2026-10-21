from fastapi import FastAPI

app = FastAPI()

@app.get("/teapot", status_code=418)
def teapot():
  return "I'm a teapot"
