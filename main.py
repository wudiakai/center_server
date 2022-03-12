from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from markdownReader import read_markdown

app = FastAPI()

origins = [
    # "http://10.1.29.11",
    "http://10.1.29.11:8088",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Response(BaseModel):
    msg: str = 'ok'
    code: int = 200
    data: str = ''


@app.get("/markdown/{name}", response_model=Response)
async def get_markdown(name: str):
    f: str = read_markdown(name)
    if len(f) == 0:
        return {"msg": 'err: can not find file', 'code': 400, 'data': ''}
    else:
        return {'msg': 'ok', 'code': 200, 'data': f}


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=2022, debug=True)
