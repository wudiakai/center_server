from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from markdownReader import read_markdown, read_markdown_list
from timer import startMarkdownSync

app = FastAPI()

origins = [
    # "http://10.1.29.11",
    "http://10.1.29.11:8088",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8088",
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
        return {'data': ''}
    else:
        return {'data': f}

@app.get("/markdown_list")
async def get_markdown_list():
    return read_markdown_list()



@app.get("/")
async def root():
    return {"message": "Hello World"}


def init():
    startMarkdownSync()


if __name__ == '__main__':
    init()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2022, debug=True)
