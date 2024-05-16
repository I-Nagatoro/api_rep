import uvicorn
from fastapi import FastAPI

app = FastAPI()


def hello_world():
    return "Hello, world!"


@app.get("/")
async def root():
    return hello_world()


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
