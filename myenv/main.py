import fastapi
import uvicorn

print("Hello FastAPI")

api = fastapi.FastAPI()
#use alt-enter for context help

@api.get("/")
def index():
    return {"msg": "Hello From FastAPI"}

uvicorn.run(api, port=7000)